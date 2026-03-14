# Fitbit Data Analysis Pipeline

## Project Overview

An end-to-end data pipeline that extracts, cleans, and analyzes
Fitbit fitness tracker data to explore the relationship between
physical activity, sleep quality, and calories burned.

## Dataset

[Fitbit Fitness Tracker Data](https://www.kaggle.com/datasets/arashnic/fitbit) (Kaggle)  
30 users | April–May 2016 | 18 CSV files

The dataset includes:

- Daily activity & steps
- Hourly steps
- Heart rate (per second)
- Sleep logs
- Weight logs

## Project Structure

```
fitbit_project/
├── src/
│   ├── extract.py        # Load raw CSVs
│   └── transform.py      # Clean & rename columns
├── data/
│   ├── raw/              # Original Kaggle files
│   └── clean/            # Processed CSVs
├── analysis.ipynb        # SQL queries & findings
├── run_pipeline.py       # Run full ETL pipeline
├── requirements.txt
└── README.md
```

## Pipeline Steps

1. **Extract** — Load raw CSV files
2. **Transform** — Clean data (dedup, rename, feature engineering)
3. **Load** — Export to CSV and MySQL database

## Key Findings

- Average **7,638 steps/day** (below the 10,000 recommendation)
- Highly active users sleep **less** (6.6 hrs) than low-activity users (7.6 hrs)
- Peak activity hours: **6–7 PM** and **12 PM**
- Users spend avg **39 minutes awake in bed** — indicating poor sleep quality
- More steps generally correlates with more calories burned

## Technologies

- Python, Pandas, SQLAlchemy
- MySQL, PyMySQL
- Jupyter Notebook

## How to Run

```bash
pip install -r requirements.txt
python run_pipeline.py
```

## Author

Chen Shmila | Data Engineering Project
