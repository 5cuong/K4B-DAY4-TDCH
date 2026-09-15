from __future__ import annotations

import json
import re
from datetime import date
from typing import Any

from tools._shared import ROOT


ASSET_FILE = ROOT / "helpdesk_data" / "assets.json"
PLAN_FILE = ROOT / "helpdesk_data" / "warranty_plans.json"

ASSET_ID_PATTERN = re.compile(
    r"^(?:LT|DT|MB|PR|RM)-\d+$",
    re.IGNORECASE,
)


def check_warranty(asset_id: str = "") -> dict[str, Any]:
    if not isinstance(asset_id, str):
        return {
            "tool": "check_warranty",
            "error": "invalid_asset_id",
        }

    normalized_id = asset_id.strip().upper()

    if not ASSET_ID_PATTERN.fullmatch(normalized_id):
        return {
            "tool": "check_warranty",
            "error": "invalid_asset_id",
        }

    try:
        inventory = json.loads(
            ASSET_FILE.read_text(encoding="utf-8")
        )

        asset = next(
            (
                item
                for item in inventory["assets"]
                if item["asset_id"] == normalized_id
            ),
            None,
        )

        if asset is None:
            return {
                "tool": "check_warranty",
                "asset_id": normalized_id,
                "error": "asset_not_found",
            }

        warranty_until = asset.get("warranty_until")

        if not warranty_until:
            return {
                "tool": "check_warranty",
                "asset_id": normalized_id,
                "error": "warranty_not_available",
            }

        # Use the inventory snapshot date for reproducible results.
        as_of = date.fromisoformat(
            inventory["snapshot_at"][:10]
        )
        end_date = date.fromisoformat(warranty_until)

        days_until_expiry = (end_date - as_of).days
        active = days_until_expiry >= 0

        plan_data = json.loads(
            PLAN_FILE.read_text(encoding="utf-8")
        )
        plan = plan_data["plans"].get(normalized_id)

        coverage: list[str] = []
        exclusions: list[str] = []
        support_channel = None

        if plan is not None:
            coverage = plan["coverage"]
            exclusions = plan["exclusions"]
            support_channel = plan["support_channel"]

            valid_lists = all(
                isinstance(values, list)
                and all(isinstance(value, str) for value in values)
                for values in (coverage, exclusions)
            )

            if not valid_lists or not isinstance(
                support_channel, str
            ):
                raise ValueError("Invalid warranty plan")

        if not active:
            next_step = (
                "Bảo hành đã hết hạn theo snapshot. "
                "Liên hệ Helpdesk để đánh giá phương án sửa chữa."
            )
        elif plan is None:
            next_step = (
                "Còn hạn theo snapshot nhưng chưa có dữ liệu phạm vi. "
                "Liên hệ Helpdesk để xác minh điều kiện bảo hành."
            )
        else:
            next_step = (
                "Còn hạn theo snapshot. Liên hệ Helpdesk để đối chiếu "
                "sự cố với phạm vi và điều kiện bảo hành."
            )

        return {
            "tool": "check_warranty",
            "asset_id": normalized_id,
            "status": "active" if active else "expired",
            "warranty_until": end_date.isoformat(),
            "as_of": as_of.isoformat(),
            "days_remaining": max(0, days_until_expiry),
            "coverage_status": (
                "available" if plan is not None else "not_available"
            ),
            "coverage": coverage,
            "exclusions": exclusions,
            "support_channel": support_channel,
            "next_step": next_step,
            "source": "fictional_local_warranty_data",
            "notice": (
                "Kết quả tính theo snapshot giả lập; "
                "không phải xác nhận chấp thuận bảo hành từ hãng."
            ),
        }

    except (
        OSError,
        ValueError,
        KeyError,
        TypeError,
        AttributeError,
        StopIteration,
    ):
        return {
            "tool": "check_warranty",
            "asset_id": normalized_id,
            "error": "data_error",
            "message": "Không đọc được dữ liệu bảo hành hợp lệ.",
        }