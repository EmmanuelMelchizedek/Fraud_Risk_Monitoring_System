-- Fraud rate and loss by segment
SELECT merchant_category, channel,
       COUNT(*) AS transactions,
       ROUND(AVG(is_fraud) * 100, 2) AS fraud_rate,
       ROUND(SUM(chargeback_loss), 2) AS chargeback_loss
FROM transactions
GROUP BY merchant_category, channel
ORDER BY fraud_rate DESC, chargeback_loss DESC;

-- High velocity patterns
SELECT DATE(event_ts) AS event_date,
       AVG(velocity_24h) AS avg_velocity,
       SUM(is_fraud) AS confirmed_fraud
FROM transactions
GROUP BY DATE(event_ts)
ORDER BY event_date;
