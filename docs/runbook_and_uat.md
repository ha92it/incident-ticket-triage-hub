
# Operational Runbook & UAT Checklist

## 1. Triage & Escalation Runbook

### Severity & Status Handling
- **Critical + Escalated / Open:** Immediate triage, verify active owner, check SLA elapsed time vs. target, and post status updates to relevant stakeholders.
- **High + Security Alert / Vendor Delay:** Review alert/ticket details, verify whether external vendor or internal team owns resolution, and track SLA closely.
- **Medium / Low:** Process in standard queue order unless SLA breach is imminent or business impact increases.

### Communication & SLA Follow-Up
- When `actual_mins > sla_target_mins` (`BREACH`), flag the item in status updates and confirm next action/ETA with the responsible owner or outsourced vendor.
- Once resolved, record root cause and note any rule, workflow, or documentation updates required.

## 2. User Acceptance Testing (UAT) Cases

| Test ID | Scenario | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| **UAT-01** | Run `python triage_and_report.py` with valid `data/mock_tickets_alerts.csv` | Script exits with status `0` and generates `reports/daily_summary.md` | Pass |
| **UAT-02** | Dataset includes `Critical` and `Escalated` records | Records appear in the **Priority Triage & Escalation Queue** ordered by severity | Pass |
| **UAT-03** | Dataset includes a record where `actual_mins > sla_target_mins` | Record is marked `(BREACH)` and listed under **SLA Breach & Action Notes** | Pass |
| **UAT-04** | Push changes to GitHub | GitHub Actions workflow runs syntax check, secret scan, script execution, and uploads report artifact | Pass |
