CREATE TABLE weight_log (
    user_id BIGINT,
    date DATETIME,
    weight_kg FLOAT,
    bmi FLOAT,
    manual_report BOOLEAN,
    log_id BIGINT,
    missing_weight BOOLEAN,
    PRIMARY KEY (log_id)
);
