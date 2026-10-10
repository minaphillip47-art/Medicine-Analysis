# Medicine Price Analysis Dashboard

An end-to-end medicine price analysis project combining web scraping, data preparation, and an interactive Power BI dashboard. The project is designed to explore medicine prices, compare current and previous prices, and analyze pricing across medicine types and pharmaceutical companies.

## Project Overview

Medicine prices can vary across products and manufacturers. This project collects medicine listing data from Dawaagate and presents it in Power BI to make price comparisons and company-level analysis easier.

The Power BI report contains two main pages:

### 1. Medicine Analysis
- Select and filter individual medicines.
- Compare current prices with previous prices.
- Review percentage price changes.
- Explore price comparisons through charts.
- Analyze price values over the available dates in the dataset.

### 2. Companies Analysis
- Filter the report by pharmaceutical company.
- Compare medicine types across companies.
- Explore company-level price distribution using a treemap.
- View summary cards for company and medicine-type insights.

## Data Collection

Python and web-scraping techniques were used to collect medicine information from Dawaagate. The scraping workflow was designed around fields such as:

- Medicine name
- Medicine type
- Company / manufacturer
- Current price
- Previous price, when available

Some products may not display a previous price. The scraper should therefore handle missing old-price elements without interrupting the collection process.

> **Note:** Website content and prices can change. Confirm that scraping complies with the source website's terms and applicable rules, and rerun the collection process when updated data is needed.

## Tools & Technologies

- **Python** — web scraping and data collection
- **BeautifulSoup** — parsing HTML elements
- **Pandas** — organizing data into a tabular format and exporting to Excel
- **Microsoft Power BI** — interactive reporting and visualization
- **DAX** — calculated metrics and date-related analysis
- **Excel** — intermediate data storage and exchange

## Workflow

1. Collect medicine listing information from the source website.
2. Parse the relevant HTML elements and handle missing values.
3. Structure the extracted records and export them to Excel.
4. Load the data into Power BI and prepare it for analysis.
5. Build interactive report pages for medicine-level and company-level insights.

## How to Use

1. Clone or download this repository.
2. Open the Python scraper and install its required dependencies.
3. Run the scraper to collect the available medicine data and export the dataset.
4. Open `Medicine analysis.pbix` in Power BI Desktop.
5. If you refresh with a new dataset, update the file/source path and verify the column names and data types before refreshing the report.

Example dependency installation:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

The exact steps may vary depending on the final scraper implementation and data source structure.

## Repository Contents

Suggested repository structure:

```text
Medicine-Analysis/
├── Medicine analysis.pbix
├── scraper.py
├── medicines.xlsx
└── README.md
```

Include the scraper and dataset in the repository only if you intend to share them. If the dataset is large, frequently changing, or subject to website restrictions, consider providing a small sample dataset instead.

## Notes & Limitations

- Previous prices may be unavailable for some medicines.
- The dashboard reflects the data collected at the time the scraper was run; it does not automatically guarantee real-time prices.
- Website HTML structures can change, so scraping selectors may need maintenance.
- Validate extracted values and currency/number formats before using them for analysis.

## Author

Created as a data analytics project demonstrating web scraping, data preparation, and interactive dashboard development.

**Repository:** Add your GitHub repository URL here.
