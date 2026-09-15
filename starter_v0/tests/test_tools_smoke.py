import importlib
import inspect
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from tools import TOOL_FUNCTIONS, load_tool_declarations


ROOT = Path(__file__).resolve().parents[1]


class ToolSmokeTests(unittest.TestCase):
    def test_registry_matches_declarations(self):
        declarations = load_tool_declarations(
            ROOT / "artifacts" / "tools.yaml"
        )
        names = [item["name"] for item in declarations]

        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(set(names), set(TOOL_FUNCTIONS))

        for item in declarations:
            with self.subTest(tool=item["name"]):
                schema = item["parameters"]
                properties = set(schema.get("properties", {}))
                signature = inspect.signature(
                    TOOL_FUNCTIONS[item["name"]]
                )

                self.assertEqual(
                    properties,
                    set(signature.parameters),
                )
                self.assertTrue(
                    set(schema.get("required", [])) <= properties
                )

    def test_clarify_requires_response_type(self):
        declarations = load_tool_declarations(
            ROOT / "artifacts" / "tools.yaml"
        )
        declaration = next(
            item for item in declarations
            if item["name"] == "clarify"
        )

        self.assertIn(
            "response_type",
            declaration["parameters"]["required"],
        )

    def test_clarify_modes(self):
        examples = [
            ("text", []),
            ("yes_no", []),
            ("choice", ["production", "staging"]),
        ]

        for response_type, options in examples:
            with self.subTest(response_type=response_type):
                result = TOOL_FUNCTIONS["clarify"](
                    question="Smoke test question",
                    response_type=response_type,
                    options=options,
                )

                self.assertEqual(
                    result["response_type"], response_type
                )
                self.assertEqual(result["options"], options)
                self.assertTrue(result["awaiting_user"])

    def test_outlook_search_uses_email_category(self):
        result = TOOL_FUNCTIONS["search_kb"](
            query="Outlook profile Windows 11",
            category="email",
        )

        self.assertNotIn("error", result)
        self.assertTrue(result["results"])
        self.assertTrue(
            any(
                "outlook" in item["title"].lower()
                for item in result["results"]
            )
        )

    def test_lookup_returns_assigned_assets(self):
        result = TOOL_FUNCTIONS["lookup_user"](
            employee_id="EMP-1003"
        )

        self.assertEqual(
            result["employee"]["employee_id"],
            "EMP-1003",
        )
        self.assertEqual(
            result["employee"]["assigned_assets"],
            ["DT-031"],
        )

    def test_unknown_employee_returns_error(self):
        result = TOOL_FUNCTIONS["lookup_user"](
            employee_id="EMP-999999"
        )

        self.assertEqual(
            result["error"], "employee_not_found"
        )

    def test_device_network_diagnostics(self):
        result = TOOL_FUNCTIONS["inspect_device"](
            asset_id="LT-204",
            check="network",
        )

        self.assertNotIn("error", result)
        self.assertEqual(result["asset_id"], "LT-204")
        self.assertEqual(
            set(result["diagnostics"]), {"network"}
        )

    def test_non_asset_identifiers_return_error(self):
        for asset_id in ("EMP-1003", "laptop", "LT-999999"):
            with self.subTest(asset_id=asset_id):
                result = TOOL_FUNCTIONS["inspect_device"](
                    asset_id=asset_id
                )

                self.assertEqual(
                    result["error"], "asset_not_found"
                )

    def test_service_status(self):
        result = TOOL_FUNCTIONS["check_service_status"](
            service="vpn",
            environment="production",
        )

        self.assertNotIn("error", result)
        self.assertEqual(result["service"], "vpn")
        self.assertEqual(
            result["environment"], "production"
        )

    def test_unsupported_environment_returns_error(self):
        result = TOOL_FUNCTIONS["check_service_status"](
            service="email",
            environment="demo",
        )

        self.assertEqual(result["error"], "not_found")

    def test_policy_search(self):
        result = TOOL_FUNCTIONS["policy"](
            query="ticket confirmation",
            policy_area="ticketing",
        )

        self.assertNotIn("error", result)
        self.assertTrue(result["results"])
        self.assertTrue(result["results"][0]["source"])

    def test_report_formats_supplied_findings(self):
        result = TOOL_FUNCTIONS["format_incident_report"](
            findings=[
                {
                    "label": "VPN",
                    "detail": "Mock finding",
                    "source": "smoke test",
                }
            ],
            template="brief",
            incident_title="Smoke incident",
        )

        self.assertEqual(result["finding_count"], 1)
        self.assertIn("Mock finding", result["markdown"])
        self.assertIn("Smoke incident", result["markdown"])

    def test_ticket_confirmation_controls_writes(self):
        module = importlib.import_module(
            "tools.create_ticket.tool"
        )

        with TemporaryDirectory() as temporary:
            ticket_dir = Path(temporary) / "tickets"

            with patch.object(module, "TICKET_DIR", ticket_dir):
                for confirmation in (False, "true"):
                    with self.subTest(
                        confirmation=confirmation
                    ):
                        result = module.create_ticket(
                            summary="Mock VPN incident",
                            priority="high",
                            asset_id="LT-204",
                            confirmed=confirmation,
                        )

                        self.assertEqual(
                            result["status"],
                            "needs_confirmation",
                        )
                        self.assertFalse(ticket_dir.exists())

                result = module.create_ticket(
                    summary="Mock VPN incident",
                    priority="high",
                    asset_id="LT-204",
                    confirmed=True,
                )

                self.assertEqual(result["status"], "created")
                self.assertTrue(Path(result["path"]).is_file())
                self.assertEqual(
                    len(list(ticket_dir.glob("*.json"))),
                    1,
                )

    def test_invalid_ticket_inputs_do_not_write(self):
        module = importlib.import_module(
            "tools.create_ticket.tool"
        )

        examples = [
            ({"summary": ""}, "missing_summary"),
            (
                {"priority": "urgent"},
                "invalid_priority",
            ),
            (
                {"asset_id": "EMP-1003"},
                "invalid_asset_id",
            ),
            (
                {"summary": "password=FAKE_SMOKE_ONLY"},
                "restricted_sensitive_data",
            ),
        ]

        with TemporaryDirectory() as temporary:
            ticket_dir = Path(temporary) / "tickets"

            with patch.object(module, "TICKET_DIR", ticket_dir):
                for overrides, expected_error in examples:
                    with self.subTest(error=expected_error):
                        arguments = {
                            "summary": "Mock VPN incident",
                            "priority": "medium",
                            "asset_id": "LT-204",
                            "confirmed": True,
                        }
                        arguments.update(overrides)

                        result = module.create_ticket(**arguments)

                        self.assertEqual(
                            result["error"], expected_error
                        )
                        self.assertFalse(ticket_dir.exists())

    def test_web_blocks_internal_id_before_http(self):
        module = importlib.import_module(
            "tools.search_device_info.tool"
        )

        with patch.object(module.requests, "post") as post:
            result = module.search_device_info(
                manufacturer="Lenovo",
                model="LT-204",
                query_type="support",
            )

            self.assertEqual(
                result["error"],
                "restricted_internal_identifier",
            )
            post.assert_not_called()


if __name__ == "__main__":
    unittest.main()