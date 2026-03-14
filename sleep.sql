CREATE TABLE sleep (
    user_id BIGINT,
    sleep_date DATETIME,
    total_sleep_records INT,
    minutes_asleep INT,
    minutes_in_bed INT,
    minutes_awake_in_bed INT,
    incomplete BOOLEAN,
    PRIMARY KEY (user_id, sleep_date)
);
