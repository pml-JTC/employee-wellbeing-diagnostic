# Employee Well-Being Diagnostic Tool

A command-line interface (CLI) application that calculates burnout and mental health risk scores for employees. This prototype sketch serves as a baseline for a more intricate and responsive tool that would use live data and be tailored to specific parameters for different companies or organizations interested in optimizing the productivity of their teams. It analyzes labor burden, local cost-of-living metrics, and demographic stress factors, then outputs a formatted visual report using the `rich` library. (This sketch uses a local data csv in place of an online database to keep things simple.)

My interest in this project comes from a deep interest in advancing mental healthcare from a field that contains or defines people without considering first and foremost their economic viability. The true measure of "functional" has to be with respect to one's ability to hold down a job, and conversely, without means a person cannot hope to maintain true mental health for very long. Employers could use a more complex, individualized version of this prototype sketch to ensure that their employees are not working in conditions that lead to burnout. Advances in computational psychiatry are already driving employer-led initiatives into maintaining the mental health of their own workforces, without deferring to the insurance gate-keeping still tightly linked to the APA's DSM coding system. As long as that infrastructure is in place, workforces and the profit their work produces will be exposed to unnecessary risk. This tool can serve as a starting point for iterating useful tools tailored to specific companies. A company's fiscal health cannot be decoupled from the mental well-being of its employees.

#### Video Demo: 

## Features

- **Local Cost-of-Living Integration**: Pulls average rent and salary data from a CSV file to evaluate local economic stress.
- **Risk Score Algorithm**: Calculates a metric from 0 to 100 based on International Labour Organization (ILO) standards for working hours, rent-to-income ratios, and age brackets.
- **Strict Input Validation**: Validates user inputs (age, income, hours, city names) to prevent faulty analysis (these parameters would be tailored to each client's needs in a product version).
- **Rich Terminal UI**: Generates clean visual progress bars, tabular reports, and color-coded status panels (a product version would generate a dashboard on a proper web/app UI).

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


## Prototype Scope & Boundaries
- **Geographic Data Limitation**: Because this prototype is restricted to offline execution, `data.csv` contains a sample dataset of US regional metrics.
- **Input Validation**: The current string validation ensures structural integrity (characters only). It does not validate global geographic accuracy (e.g., matching "Oslo, Sweden"). In a production version, this boundary would be resolved by replacing the local CSV lookup with a live global geolocation API.


## Usage

Run the script from your terminal:

```bash
python project.py
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

## Testing
To run the automated test suite, ensure you have `pytest` installed:
```bash
pip install pytest
```
Execute the tests from the root directory:
```bash
pytest test_project.py
```

## License

This project is licensed under the MIT License - see the text below for details:

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


