CREATE TABLE heartrate_seconds (
    user_id BIGINT,
    timestamp DATETIME,
    heartrate INT,
    incomplete BOOLEAN,
    flag BOOLEAN,
    PRIMARY KEY (user_id, timestamp)
);
