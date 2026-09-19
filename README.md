# CSV Insights Tool

A web-based data analysis app built with Python and Streamlit. Upload any CSV file to instantly explore, clean, analyze, visualize, uncover correlations, and export your data — no code required.

**Live demo:** [csv-insights-tool-lars-liguori.streamlit.app](https://csv-insights-tool-lars-liguori.streamlit.app)

## Features
- **Load:** Upload any CSV file through the browser
- **Overview:** View dataset shape (rows/columns) and missing-value counts
- **Clean:** Handle missing values (drop rows or fill with 0)
- **Analyze:** Select any column for statistical summaries
- **Visualize:** Auto-generated charts, adapting to numeric vs. categorical columns
- **Database:** Save uploaded data to a local SQLite database and preview the top 10 records
- **Correlation:** Analyze relationships between numeric columns with an interactive correlation matrix and heatmap
- **Export:** Download the cleaned dataset as a CSV

## Built With
- Python
- Streamlit
- Pandas
- matplotlib
- seaborn
- numpy
- sqlite3

## Run Locally
```bash
git clone https://github.com/Ligsly22/csv-insights-tool.git
cd csv-insights-tool
pip install -r requirements.txt
streamlit run CSV_insights_tool.py
```