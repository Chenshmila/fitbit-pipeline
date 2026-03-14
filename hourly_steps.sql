CREATE TABLE hourly_steps (
    user_id BIGINT,
    activity_hour DATETIME,
    steps INT,
    hour INT,
    day DATE,
    PRIMARY KEY (user_id, activity_hour)
);
