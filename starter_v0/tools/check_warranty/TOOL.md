---
name: check_warranty
track: bonus
kind: local_inventory
provider: fictional_warranty_data
requires_env: []
inputs: [asset_id]
outputs: [asset_id, status, warranty_until, as_of, days_remaining, coverage_status, coverage, exclusions, support_channel, next_step, source, notice]
side_effect: false
---
# check_warranty

Checks a fictional company asset's warranty using local data.

The expiration date comes from `helpdesk_data/assets.json`.
Coverage information comes from `helpdesk_data/warranty_plans.json`.

Status is calculated at the inventory snapshot date, not the current date.
A warranty remains active on its expiration date.

The tool returns active/expired status, days remaining, available coverage,
exclusions, and a suggested next step. Missing coverage is reported explicitly.

Errors:
- invalid_asset_id
- asset_not_found
- warranty_not_available
- data_error

This tool does not contact vendors, write files, create claims, or guarantee
that a particular incident will be accepted under warranty.