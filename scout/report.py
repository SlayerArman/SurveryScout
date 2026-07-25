from datetime import datetime
from pathlib import Path

def save_report(lines):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    filename = reports_dir / f"report-{datetime.now():():%Y%m%d-%H%M%S}.txt"

    with filename.open("w", encoding="utf-8") as report:
        report.write("Operation Scout\n")
        report.write("=" * 40 + "\n")
        report.write(
            f"Generated: {datetime.now().strfttime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        for line in lines:
            report.write(line + "\n")

    return filename