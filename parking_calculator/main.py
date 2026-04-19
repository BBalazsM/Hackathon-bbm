from pathlib import Path
from datetime import datetime
import math

FREE_MINUTES = 30
DAY_MINUTES = 24 * 60
DAY_FEE = 10000

def parse_dt(s: str):
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")

def partial_fee(m):
    if m <= FREE_MINUTES:
        return 0
    h = math.ceil((m - FREE_MINUTES) / 60)
    return min(h, 3) * 300 + max(h - 3, 0) * 500

def calculate_fee(total_minutes: int) -> int:
    if total_minutes <= FREE_MINUTES:
        return 0
    days = total_minutes // DAY_MINUTES
    rest = total_minutes % DAY_MINUTES
    total = days * DAY_FEE
    total += partial_fee(rest)
    return total

def format_duration(total_minutes: int) -> str:
    hours = total_minutes // 60
    minutes = total_minutes % 60
    parts = []
    if hours > 0:
        parts.append(f"{hours} óra")
    if minutes > 0:
        parts.append(f"{minutes} perc")
    return " ".join(parts) if parts else "0 perc"

def process_line(line: str):
    try:
        parts = line.split()
        start = parse_dt(" ".join(parts[1:3]))
        end = parse_dt(" ".join(parts[3:5]))

        if end < start:
            return "HIBA"

        total_minutes = int((end - start).total_seconds() // 60)
        fee = calculate_fee(total_minutes)
        duration = format_duration(total_minutes)

        return f"{duration} parkolás → {fee} Ft"
    except:
        return "HIBA"

def main():
    lines = Path("input.txt").read_text(encoding="utf-8").splitlines()

    for line in lines:
        line = line.strip()
        if not line or "RENDSZAM" in line or "=" in line:
            continue

        print(process_line(line))

if __name__ == "__main__":
    main()
