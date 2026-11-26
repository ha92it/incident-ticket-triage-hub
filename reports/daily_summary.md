# Incident & Ticket Triage — Operational & Security Summary

**Generated At:** 2026-11-26 10:38 UTC
**Source Dataset:** `data/mock_tickets_alerts.csv`

## 1. Executive KPIs

- **Total Records Analyzed:** 8
- **SLA Compliance Rate:** 62.5% (5/8 within target SLA)
- **SLA Breaches Detected:** 3
- **High / Critical Items:** 4 (Critical: 2, High: 2)
- **Escalated Items:** 2

## 2. Breakdown by Status & Category

### By Status
- **Escalated:** 2
- **In Progress:** 2
- **Open:** 3
- **Resolved:** 1

### By Category
- **Incident:** 1
- **Security Alert:** 3
- **Support Ticket:** 3
- **Vendor Delay:** 1

## 3. Priority Triage & Escalation Queue

| ID | Source | Category | Severity | Status | SLA (Actual / Target) | Summary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| INC-101 | SIEM | Security Alert | Critical | Escalated | 42m / 30m (BREACH) | Multiple failed admin login attempts detected from unusual IP |
| INC-105 | SIEM | Incident | Critical | Open | 18m / 30m | High volume of blocked outbound traffic to unknown domain |
| VND-104 | Vendor-Ticket | Vendor Delay | High | Escalated | 165m / 120m (BREACH) | Outsourced support vendor delayed response on billing ticket sync |
| INC-103 | Cloud-Guard | Security Alert | High | In Progress | 55m / 60m | Suspicious IAM role policy change in staging environment |

## 4. SLA Breach & Action Notes

- **INC-101** (SIEM - Security Alert): Exceeded SLA by **12 minutes** — Status: `Escalated`. Action: Verify owner, update stakeholder status, and review bottleneck.
- **VND-104** (Vendor-Ticket - Vendor Delay): Exceeded SLA by **45 minutes** — Status: `Escalated`. Action: Verify owner, update stakeholder status, and review bottleneck.
- **TKT-108** (Vendor-Ticket - Support Ticket): Exceeded SLA by **20 minutes** — Status: `Open`. Action: Verify owner, update stakeholder status, and review bottleneck.

## 5. Recommended Next Steps

- Confirm active ownership and escalation updates for any `Escalated` or `Critical` items.
- Follow up with support/vendor owners on SLA breaches to prevent recurring delays.
- Document root causes and any workflow or rule adjustments needed after resolution.
