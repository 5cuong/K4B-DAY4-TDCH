import importlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch


module = importlib.import_module("tools.check_warranty.tool")


class WarrantyTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)

        self.root = Path(temporary.name)
        self.asset_file = self.root / "assets.json"
        self.plan_file = self.root / "plans.json"

        inventory = {
            "snapshot_at": "2026-09-15T09:00:00+07:00",
            "assets": [
                {
                    "asset_id": "LT-204",
                    "warranty_until": "2026-09-16",
                },
                {
                    "asset_id": "DT-031",
                    "warranty_until": "2026-09-14",
                },
                {
                    "asset_id": "MB-012",
                    "warranty_until": "2026-09-15",
                },
                {"asset_id": "LT-240"},
            ],
        }

        plans = {
            "plans": {
                "LT-204": {
                    "coverage": ["Mock hardware coverage"],
                    "exclusions": ["Mock accidental damage"],
                    "support_channel": "Mock Helpdesk",
                }
            }
        }

        self.asset_file.write_text(
            json.dumps(inventory), encoding="utf-8"
        )
        self.plan_file.write_text(
            json.dumps(plans), encoding="utf-8"
        )

        asset_patch = patch.object(
            module, "ASSET_FILE", self.asset_file
        )
        plan_patch = patch.object(
            module, "PLAN_FILE", self.plan_file
        )

        asset_patch.start()
        plan_patch.start()
        self.addCleanup(asset_patch.stop)
        self.addCleanup(plan_patch.stop)

    def test_active_and_normalized_id(self):
        result = module.check_warranty(" lt-204 ")

        self.assertEqual(result["asset_id"], "LT-204")
        self.assertEqual(result["status"], "active")
        self.assertEqual(result["days_remaining"], 1)
        self.assertEqual(result["as_of"], "2026-09-15")
        self.assertEqual(result["coverage_status"], "available")
        self.assertEqual(
            result["coverage"], ["Mock hardware coverage"]
        )

    def test_expired(self):
        result = module.check_warranty("DT-031")

        self.assertEqual(result["status"], "expired")
        self.assertEqual(result["days_remaining"], 0)

    def test_expiration_day_is_active(self):
        result = module.check_warranty("MB-012")

        self.assertEqual(result["status"], "active")
        self.assertEqual(result["days_remaining"], 0)

    def test_missing_plan_is_not_invented(self):
        result = module.check_warranty("MB-012")

        self.assertEqual(
            result["coverage_status"], "not_available"
        )
        self.assertEqual(result["coverage"], [])
        self.assertEqual(result["exclusions"], [])
        self.assertIsNone(result["support_channel"])

    def test_unknown_asset(self):
        result = module.check_warranty("LT-999999")

        self.assertEqual(result["error"], "asset_not_found")

    def test_missing_warranty_date(self):
        result = module.check_warranty("LT-240")

        self.assertEqual(
            result["error"], "warranty_not_available"
        )

    def test_invalid_inputs(self):
        for value in ("", "laptop", "EMP-1003", None, 123):
            with self.subTest(value=value):
                result = module.check_warranty(value)
                self.assertEqual(
                    result["error"], "invalid_asset_id"
                )

    def test_invalid_data(self):
        self.asset_file.write_text(
            '{"assets":', encoding="utf-8"
        )

        result = module.check_warranty("LT-204")
        self.assertEqual(result["error"], "data_error")

    def test_missing_plan_file(self):
        with patch.object(
            module,
            "PLAN_FILE",
            self.root / "missing.json",
        ):
            result = module.check_warranty("LT-204")

        self.assertEqual(result["error"], "data_error")

    def test_read_only_and_stable(self):
        before = {
            path.name: path.read_bytes()
            for path in self.root.iterdir()
        }

        first = module.check_warranty("LT-204")
        second = module.check_warranty("LT-204")

        after = {
            path.name: path.read_bytes()
            for path in self.root.iterdir()
        }

        self.assertEqual(first, second)
        self.assertEqual(before, after)
        json.dumps(first)


if __name__ == "__main__":
    unittest.main()