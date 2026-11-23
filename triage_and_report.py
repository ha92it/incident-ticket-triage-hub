import csv
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_CSV = BASE_DIR / "data" / "mock_tickets_alerts.csv"
OUTPUT_MD = BASE_DIR / "reports" / "daily_summary.md"

SEVERITY_ORDER = {
    "Critical": 1,
    "High": 2,
    "Medium": 3,
    "Low": 4,
}


def load_records(csv_path: Path) -> list[dict]:
    with csv_path.open(mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        records = []
        for row in reader:
            row["sla_target_mins"] = int(row["sla_target_mins"])
            row["actual_mins"] = int(row["actual_mins"])
            row["sla_breached"] = row["actual_mins"] > row["sla_target_mins"]
            records.append(row)
    return records


def generate_report(records: list[dict]) -> str:
    total = len(records)
    severity_counts = Counter(r["severity"] for r in records)
    status_counts = Counter(r["status"] for r in records)
    category_counts = Counter(r["category"] for r in records)

    breached_items = [r for r in records if r["sla_breached"]]
    sla_met_count = total - len(breached_items)
    sla_compliance_pct = (sla_met_count / total * 100) if total else 0.0

    priority_queue = [
        r
        for r in records
        if r["severity"] in {"Critical", "High"} or r["status"] == "Escalated"
    ]
    priority_queue.sort(
        key=lambda r: (
            SEVERITY_ORDER.get(r["severity"], 99),
            0 if r["status"] == "Escalated" else 1,
            r["id"],
        )
    )

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Incident & Ticket Triage — Operational & Security Summary",
        "",
        f"**Generated At:** {now_str}",
        f"**Source Dataset:** `{INPUT_CSV.relative_to(BASE_DIR)}`",
        "",
        "## 1. Executive KPIs",
        "",
        f"- **Total Records Analyzed:** {total}",
        f"- **SLA Compliance Rate:** {sla_compliance_pct:.1f}% ({sla_met_count}/{total} within target SLA)",
        f"- **SLA Breaches Detected:** {len(breached_items)}",
        f"- **High / Critical Items:** {severity_counts['High'] + severity_counts['Critical']} "
        f"(Critical: {severity_counts['Critical']}, High: {severity_counts['High']})",
        f"- **Escalated Items:** {status_counts['Escalated']}",
        "",
        "## 2. Breakdown by Status & Category",
        "",
        "### By Status",
    ]

    for status, count in sorted(status_counts.items()):
        lines.append(f"- **{status}:** {count}")

    lines.extend(["", "### By Category"])
    for category, count in sorted(category_counts.items()):
        lines.append(f"- **{category}:** {count}")

    lines.extend(
        [
            "",
            "## 3. Priority Triage & Escalation Queue",
            "",
            "| ID | Source | Category | Severity | Status | SLA (Actual / Target) | Summary |",
            "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        ]
    )

    for item in priority_queue:
        sla_label = f"{item['actual_mins']}m / {item['sla_target_mins']}m"
        if item["sla_breached"]:
            sla_label += " (BREACH)"
        lines.append(
            f"| {item['id']} | {item['source']} | {item['category']} | "
            f"{item['severity']} | {item['status']} | {sla_label} | {item['summary']} |"
        )

    lines.extend(["", "## 4. SLA Breach & Action Notes", ""])
    if not breached_items:
        lines.append("- All records are currently within their defined SLA targets.")
    else:
        for item in breached_items:
            over_by = item["actual_mins"] - item["sla_target_mins"]
            lines.append(
                f"- **{item['id']}** ({item['source']} - {item['category']}): "
                f"Exceeded SLA by **{over_by} minutes** — Status: `{item['status']}`. "
                f"Action: Verify owner, update stakeholder status, and review bottleneck."
            )

    lines.extend(
        [
            "",
            "## 5. Recommended Next Steps",
            "",
            "- Confirm active ownership and escalation updates for any `Escalated` or `Critical` items.",
            "- Follow up with support/vendor owners on SLA breaches to prevent recurring delays.",
            "- Document root causes and any workflow or rule adjustments needed after resolution.",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    if not INPUT_CSV.exists():
        raise FileNotFoundError(f"Input CSV not found at: {INPUT_CSV}")

    records = load_records(INPUT_CSV)
    report_content = generate_report(records)

    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD.write_text(report_content, encoding="utf-8")
    print(f"Report generated successfully at: {OUTPUT_MD}")


if __name__ == "__main__":
    main()
