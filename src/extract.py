import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "raw")


def load_daily_activity():
    return pd.read_csv(os.path.join(DATA_PATH, "dailyActivity_merged.csv"))


def load_daily_calories():
    return pd.read_csv(os.path.join(DATA_PATH, "dailyCalories_merged.csv"))


def load_daily_intensities():
    return pd.read_csv(os.path.join(DATA_PATH, "dailyIntensities_merged.csv"))


def load_daily_steps():
    return pd.read_csv(os.path.join(DATA_PATH, "dailySteps_merged.csv"))


def load_heartrate_seconds():
    return pd.read_csv(os.path.join(DATA_PATH, "heartrate_seconds_merged.csv"))


def load_hourly_calories():
    return pd.read_csv(os.path.join(DATA_PATH, "hourlyCalories_merged.csv"))


def load_hourly_intensities():
    return pd.read_csv(os.path.join(DATA_PATH, "hourlyIntensities_merged.csv"))


def load_hourly_steps():
    return pd.read_csv(os.path.join(DATA_PATH, "hourlySteps_merged.csv"))


def load_minute_calories_narrow():
    return pd.read_csv(os.path.join(DATA_PATH, "minuteCaloriesNarrow_merged.csv"))


def load_minute_calories_wide():
    return pd.read_csv(os.path.join(DATA_PATH, "minuteCaloriesWide_merged.csv"))


def load_minute_intensities_narrow():
    return pd.read_csv(os.path.join(DATA_PATH, "minuteIntensitiesNarrow_merged.csv"))


def load_minute_intensities_wide():
    return pd.read_csv(os.path.join(DATA_PATH, "minuteIntensitiesWide_merged.csv"))


def load_minute_mets_narrow():
    return pd.read_csv(os.path.join(DATA_PATH, "minuteMETsNarrow_merged.csv"))


def load_minute_sleep():
    return pd.read_csv(os.path.join(DATA_PATH, "minuteSleep_merged.csv"))


def load_minute_steps_narrow():
    return pd.read_csv(os.path.join(DATA_PATH, "minuteStepsNarrow_merged.csv"))


def load_minute_steps_wide():
    return pd.read_csv(os.path.join(DATA_PATH, "minuteStepsWide_merged.csv"))


def load_sleep_day():
    return pd.read_csv(os.path.join(DATA_PATH, "sleepDay_merged.csv"))


def load_weight_log_info():
    return pd.read_csv(os.path.join(DATA_PATH, "weightLogInfo_merged.csv"))
