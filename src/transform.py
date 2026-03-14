import pandas as pd


def clean_daily_activity(df):
    df = df.rename(
        columns={
            "Id": "user_id",
            "ActivityDate": "activity_date",
            "TotalSteps": "total_steps",
            "Calories": "calories",
        }
    )
    df["activity_date"] = pd.to_datetime(df["activity_date"])
    df["incomplete"] = (df["total_steps"] == 0) | (df["calories"] == 0)
    df["calories_per_step"] = df["calories"].div(df["total_steps"].replace(0, pd.NA))
    return df


def clean_sleep_day(df):
    df = df.drop_duplicates(subset=["Id", "SleepDay"])
    df = df.copy()
    df["SleepDay"] = pd.to_datetime(
        df["SleepDay"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce"
    )
    df = df.rename(
        columns={
            "Id": "user_id",
            "SleepDay": "sleep_date",
            "TotalSleepRecords": "total_sleep_records",
            "TotalMinutesAsleep": "minutes_asleep",
            "TotalTimeInBed": "minutes_in_bed",
        }
    )
    df["date"] = df["sleep_date"].dt.date
    df["minutes_awake_in_bed"] = df["minutes_in_bed"] - df["minutes_asleep"]
    df["incomplete"] = (df["minutes_asleep"] == 0) | (df["minutes_in_bed"] == 0)
    return df


def clean_hourly_steps(df):
    df["ActivityHour"] = pd.to_datetime(
        df["ActivityHour"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce"
    )
    df = df.rename(
        columns={"Id": "user_id", "ActivityHour": "activity_hour", "StepTotal": "steps"}
    )
    df["hour"] = df["activity_hour"].dt.hour
    df["day"] = df["activity_hour"].dt.date
    return df


def clean_heartrate_seconds(df):
    df["Time"] = pd.to_datetime(
        df["Time"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce"
    )
    df["incomplete"] = df["Value"] == 0
    df["flag"] = (df["Value"] == 0) | (df["Value"] < 40) | (df["Value"] > 200)
    df = df.rename(columns={"Id": "user_id", "Time": "timestamp", "Value": "heartrate"})
    return df


def clean_weight_log_info(df):
    df = df.drop(columns=["Fat"])
    df = df.drop(columns=["WeightPounds"])
    df["Date"] = pd.to_datetime(
        df["Date"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce"
    )
    df["missing_weight"] = df["WeightKg"] == 0
    df = df.rename(
        columns={
            "Id": "user_id",
            "Date": "date",
            "WeightKg": "weight_kg",
            "BMI": "bmi",
            "IsManualReport": "manual_report",
            "LogId": "log_id",
        }
    )
    return df
