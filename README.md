# Employee Well-Being Diagnostic Tool

A command-line interface (CLI) application that calculates burnout and mental health risk scores for employees. It analyzes labor burden, local cost-of-living metrics, and demographic stress factors, then outputs a formatted visual report using the `rich` library.

#### Video Demo:  <URL HERE>

## Features

- **Local Cost-of-Living Integration**: Pulls average rent and salary data from a CSV file to evaluate local economic stress.
- **Risk Score Algorithm**: Calculates a metric from 0 to 100 based on International Labour Organization (ILO) standards for working hours, rent-to-income ratios, and age brackets.
- **Strict Input Validation**: Validates user inputs (age, income, hours, city names) to prevent faulty analysis.
- **Rich Terminal UI**: Generates clean visual progress bars, tabular reports, and color-coded status panels.

## Prerequisites

Before running the tool, ensure you have Python installed along with the required dependencies:

```bash
pip install pandas rich
```

## Data Setup

The tool expects a local file named `data.csv` in the same directory to fetch regional metrics. The CSV must include the following column headers:
- `city`
- `rent_1br_city_center_usd`
- `median_salary_net_usd_monthly`

*Note: If `data.csv` is missing or empty, the application will automatically fall back to standard baseline metrics.*

## Usage

Run the script from your terminal:

```bash
python main.py
```

### Example Walkthrough

1. **Provide Inputs**: The CLI will prompt you for demographic and work data.
   ```text
   ========================================
    EMPLOYEE WELL-BEING DIAGNOSTIC TOOL
   ========================================
   City: New York
   Age: 25
   Annual Gross Income (\$): 65,000
   Weekly Hours Worked: 55
   ```

2. **Validation Constraints**:
   - **City**: Text characters only.
   - **Age**: Must be between 18 and 90.
   - **Hours**: Must be between 20 and 80 hours per week.
   - **Income**: Must be a minimum of $20,000 annually.

3. **Output Report**: The tool displays a stylized dashboard with your final risk status assessment (Stable, Elevated, or Critical).

## Code Structure

- `MentalHealthAPI`: A class handling CSV loading and matching local financial stats to the user's city.
- `calculate_risk_score()`: The core algorithmic function scoring labor burden, severe/moderate rent stress, and age-related risk factors.
- `get_assessment()`: Maps the numerical score to text classifications.
- `generate_visual_score()`: Builds the terminal ASCII progress bar.
- `main()`: Controls user input flow, input parsing, error handling, and UI rendering.

## License

This project is licensed under the MIT License - see the text below for details:

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


