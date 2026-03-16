# Fitbit Data Analysis Pipeline

## Project Overview

An end-to-end data pipeline that extracts, cleans, and analyzes Fitbit fitness tracker data in order to explore relationships between physical activity, sleep quality, and calorie expenditure.

The project demonstrates a simple **ETL pipeline** commonly used in data engineering workflows.

---

## Dataset

Fitbit Fitness Tracker Data (Kaggle)
30 users | April–May 2016 | 18 CSV files

The dataset includes:

* Daily activity and step counts
* Hourly step data
* Heart rate measurements (per second)
* Sleep tracking logs
* Weight tracking logs

---

## Pipeline Architecture

```
Raw CSV files
   ↓
Extract (Python)
   ↓
Transform (Pandas data cleaning & feature engineering)
   ↓
Clean CSV files
   ↓
Load to MySQL database
   ↓
SQL analysis in Jupyter Notebook
```

---

## Project Structure

```
fitbit_project/
├── src/
│   ├── extract.py        # Load raw CSV files
│   └── transform.py      # Data cleaning and feature engineering
├── data/
│   ├── raw/              # Original Kaggle files
│   └── clean/            # Processed datasets
├── analysis.ipynb        # SQL queries and analytical findings
├── run_pipeline.py       # Runs the full ETL pipeline
├── requirements.txt
└── README.md
```

---

## Pipeline Steps

### 1. Extract

Load raw CSV datasets from the Kaggle dataset.

### 2. Transform

Clean and prepare the data using Pandas:

* Rename columns
* Convert date/time formats
* Remove duplicates
* Create derived features
* Flag incomplete or suspicious data

### 3. Load

The cleaned datasets are exported to:

* Clean CSV files
* A MySQL database

---

## SQL Analysis

The project also includes SQL-based analysis and research questions examining relationships between activity levels, sleep patterns, and calories burned.

The full SQL queries and findings are available in **`analysis.ipynb`**.

---

## Key Findings

* Average **7,638 steps per day** (below the 10,000 recommendation)
* Highly active users sleep **less** (6.6 hours) than low-activity users (7.6 hours)
* Peak activity hours: **12 PM** and **6–7 PM**
* Users spend an average of **39 minutes awake in bed**
* Higher step counts generally correlate with higher calorie burn

---

## Technologies

* Python
* Pandas
* SQLAlchemy
* MySQL
* PyMySQL
* Jupyter Notebook

---

## How to Run

Install dependencies:

```
pip install -r requirements.txt
```

Run the pipeline:

```
python run_pipeline.py
```

---

## Author

Chen Shmila
Data Engineering Project
