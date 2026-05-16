import pytest
from project import calculate_risk_score, get_assessment, generate_visual_score

def test_calculate_risk_score_extreme_low_income():
    # Tests that a $20,000 salary ($1,666/mo) does not trigger rent stress
    # if rent ($1,200) is more than 50% of monthly income
    stats = {"avg_rent": 1200.0, "avg_local_salary": 4500.0}

    # 30 years old (0 pts), $20,000 income (40 pts rent stress), 40 hours (0 pts)
    score = calculate_risk_score(age=30, income=20000, hours=40, local_stats=stats)
    assert score == 50

def test_calculate_risk_score_billionaire_overwork():
    # Tests that a massive earner gets 0 rent stress points but still gets hit for overwork
    stats = {"avg_rent": 1200.0, "avg_local_salary": 4500.0}

    # 35 years old (0 pts), $1,000,000 income (0 pts rent stress), 70 hours (40 pts overwork)
    score = calculate_risk_score(age=35, income=1000000, hours=70, local_stats=stats)
    assert score == 40

def test_calculate_risk_score_max_caps():
    # Tests that scores can never mathematically exceed 100 points
    stats = {"avg_rent": 2000.0, "avg_local_salary": 4500.0}

    # 22 years old (20 pts), $24,000 income (40 pts rent stress), 80 hours (40 pts overwork) = 100 pts
    score = calculate_risk_score(age=22, income=24000, hours=80, local_stats=stats)
    assert score == 100

def test_get_assessment_boundaries():
    # Tests the exact threshold cuts for HR reporting
    assert get_assessment(100) == "CRITICAL: High risk of burnout."
    assert get_assessment(75) == "CRITICAL: High risk of burnout."
    assert get_assessment(74) == "ELEVATED: Moderate risk."
    assert get_assessment(40) == "ELEVATED: Moderate risk."
    assert get_assessment(39) == "STABLE: Risk factors are manageable."
    assert get_assessment(0) == "STABLE: Risk factors are manageable."

def test_generate_visual_score_formatting():
    # Tests the text-based loading bar outputs for the Rich table display
    assert generate_visual_score(0) == "[--------------------] 0%"
    assert generate_visual_score(50) == "[██████████----------] 50%"
    assert generate_visual_score(100) == "[████████████████████] 100%"
