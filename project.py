import sys
import pandas as pd
import re
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class MentalHealthAPI:
    def __init__(self, filename=None):
        if isinstance(filename, pd.DataFrame):
            self.df = filename
        else:
            try:
                self.df = pd.read_csv(filename)
            except Exception:
                self.df = pd.DataFrame(columns=['city', 'rent_1br_city_center_usd', 'median_salary_net_usd_monthly'])

    def get_local_metrics(self, city: str) -> dict:
        city_cleaned = city.strip().lower()

        if 'rent_1br_city_center_usd' in self.df.columns and not self.df.empty:
            match = self.df[self.df['city'].str.lower() == city_cleaned]
            if not match.empty:
                return {
                    "avg_rent": float(match['rent_1br_city_center_usd'].iloc[0]),
                    "avg_local_salary": float(match['median_salary_net_usd_monthly'].iloc[0])
                }

        return {"avg_rent": 1200.0, "avg_local_salary": 4500.0}


def calculate_risk_score(age: int, income: float, hours: int, local_stats: dict) -> int:
    """Function 1"""
    age, income, hours = max(0, age), max(0, income), max(0, hours)
    score = 0

# Labor Burden (ILO Standard: >48 hours increases health risks)
    if hours > 60:
        score += 40
    elif hours > 48:
        score += 20

    monthly_gross = income / 12
    avg_rent = local_stats['avg_rent']

# Only calculates rent stress if their income can realistically cover it
    if monthly_gross >= avg_rent:
        rent_to_income_ratio = avg_rent / monthly_gross

        if rent_to_income_ratio > 0.50:      # Severe rent burden
            score += 40
        elif rent_to_income_ratio > 0.30:    # Moderate rent burden
            score += 20

# Early career stress, sandwich generation, and young adult
    if age < 26:
        score += 20
    elif 40 < age < 50:
        score += 15
    elif age < 32:
        score += 10

    return min(score, 100)

def get_assessment(score: int) -> str:
    """Function 2"""
    if score >= 75:
        return "CRITICAL: High risk of burnout."
    if score >= 40:
        return "ELEVATED: Moderate risk."
    return "STABLE: Risk factors are manageable."

def generate_visual_score(score: int) -> str:
    """Function 3"""
    bar_length = 20
    filled_length = int(bar_length * score // 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    return f"[{bar}] {score}%"

def main():
    print("="*40)
    print(" EMPLOYEE WELL-BEING DIAGNOSTIC TOOL")
    print("="*40)

    try:
        # 1. Gather Inputs
        city = input("City: ").strip()
        age = int(input("Age: "))
        income_str = input("Annual Gross Income ($): ").replace(",", "").strip()
        income = float(income_str)
        hours = int(input("Weekly Hours Worked: "))

        # 2. Validation Block
        if not re.search(r"^[a-zA-Z\s\-,]+$", city):
            raise ValueError("Invalid characters in city name")

        city = city.split(",")[0].strip()
        if not (18 <= age <= 90):
            raise ValueError("Age out of range")
        if not (20 <= hours <= 80):
            raise ValueError("Weekly hours must be between 20 and 80 for regular staff analysis.")
        if income < 20000:
            raise ValueError("Annual gross income must be at least $20,000.")

    except ValueError as e:
        sys.exit(f"Invalid Input: {e}")

    print("\n[!] Analyzing metrics and local data...", end="", flush=True)
    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print(" DONE\n")

    # 3. Instantiate API using local data
    api = MentalHealthAPI("data.csv")
    stats = api.get_local_metrics(city)

    score = calculate_risk_score(age, income, hours, stats)
    console = Console()

    # 4. Create a nice Table
    table = Table(title=f"Diagnostic Report: {city.title()}", show_header=True, header_style="bold cyan")
    table.add_column("Category", style="dim")
    table.add_column("Result")
    table.add_row("Input Metrics", f"{age}yrs | {hours}hrs/wk | ${income:,.0f}")
    table.add_row("Risk Progress", generate_visual_score(score))
    table.add_row("Raw Score", f"{score}/100")

    # 5. Display the Table
    console.print(table)

    # 6. Final colored verdict Panel
    color = "red" if score >= 75 else "yellow" if score >= 40 else "green"
    console.print(Panel(f"[{color} bold]{get_assessment(score)}[/]", title="Status", expand=False))

if __name__ == "__main__":
    main() 
