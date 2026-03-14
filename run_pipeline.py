from src.extract import *
from src.transform import *
from sqlalchemy import create_engine
import os

os.makedirs("data/clean", exist_ok=True)

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3307/fitbit_db")

try:
    daily = clean_daily_activity(load_daily_activity())
    steps = clean_hourly_steps(load_hourly_steps())
    sleep = clean_sleep_day(load_sleep_day())
    heartrate = clean_heartrate_seconds(load_heartrate_seconds())
    weight = clean_weight_log_info(load_weight_log_info())

    daily.to_csv("data/clean/daily_activity.csv", index=False)
    steps.to_csv("data/clean/hourly_steps.csv", index=False)
    sleep.to_csv("data/clean/sleep_day.csv", index=False)
    heartrate.to_csv("data/clean/heart_rate.csv", index=False)
    weight.to_csv("data/clean/weight.csv", index=False)

    daily.to_sql("daily_activity", engine, if_exists="replace", index=False)
    steps.to_sql("hourly_steps", engine, if_exists="replace", index=False)
    sleep.to_sql("sleep", engine, if_exists="replace", index=False)
    heartrate.to_sql("heartrate_seconds", engine, if_exists="replace", index=False)
    weight.to_sql("weight_log", engine, if_exists="replace", index=False)

    print("Pipeline finished successfully")

except Exception as e:
    print(f"[ERROR] Pipeline failed: {e}")
