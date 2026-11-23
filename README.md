

# Incident & Ticket Triage Hub

A lightweight operational and security triage prototype built with Python and GitHub Actions. It ingests mock support tickets, vendor items, and security alerts, evaluates SLA adherence, prioritizes high-severity and escalated items, and generates a structured markdown summary report.

## How It Works

1. **Input Data (`data/mock_tickets_alerts.csv`):** Sample operational tickets, vendor delays, and security alerts with severity, status, and SLA targets.
2. **Triage & Reporting Engine (`triage_and_report.py`):** Calculates SLA compliance, flags SLA breaches, ranks high-priority/escalated items, and writes `reports/daily_summary.md`.
3. **CI Workflow (`.github/workflows/ci-check.yml`):** Automatically runs syntax validation, a basic secret-pattern check, and report generation on code pushes, uploading the report as an artifact.
4. **Runbook & UAT (`docs/runbook_and_uat.md`):** Documents escalation/SLA handling steps and UAT test cases.

## Running Locally

```bash
python triage_and_report.py
