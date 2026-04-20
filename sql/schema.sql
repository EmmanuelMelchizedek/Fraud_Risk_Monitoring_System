CREATE TABLE transactions (
    transaction_id BIGINT,
    event_ts TIMESTAMP,
    amount NUMERIC(12,2),
    merchant_category VARCHAR(50),
    channel VARCHAR(30),
    country_risk INTEGER,
    prior_chargebacks INTEGER,
    velocity_24h INTEGER,
    account_age_days INTEGER,
    is_weekend INTEGER,
    is_fraud INTEGER,
    chargeback_loss NUMERIC(12,2)
);
