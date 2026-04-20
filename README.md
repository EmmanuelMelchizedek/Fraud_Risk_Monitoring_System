# Fraud and Revenue Risk Monitoring Platform

## Business problem
Financial organizations need to identify suspicious transaction behavior quickly while still giving business leaders clear visibility into fraud trends, chargeback exposure, and operational risk. This project demonstrates how to combine analytics engineering, anomaly detection, and executive monitoring into one reusable risk analytics solution.

## What this project proves
- You can work with transaction-level data at scale
- You can build risk features and monitoring KPIs
- You can translate model outputs into decision-friendly reporting
- You understand fraud operations and business exposure, not just classification metrics

## Tech stack
Python, Pandas, NumPy, scikit-learn, SQL, Streamlit, Plotly, Isolation Forest, DuckDB, Docker, GitHub Actions

## Features
- Loads transaction and fraud data
- Builds risk metrics such as fraud rate, chargeback loss, high-risk segment exposure, and suspicious velocity patterns
- Runs anomaly detection to flag unusual transactions
- Produces an executive risk dashboard
- Generates a narrative summary for leadership and operations teams

## Repository structure
```text
project_2_fraud_risk_monitor/
  app/
    streamlit_app.py
  data/
    transactions.csv
  src/
    risk_features.py
    anomaly_detection.py
    summary.py
  sql/
    schema.sql
    analyst_queries.sql
  .github/workflows/
    ci.yml
  Dockerfile
  requirements.txt
```

## Local run
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Resume-ready bullets
- Built a fraud and revenue risk monitoring platform using SQL, Python, and anomaly detection to identify suspicious transaction behavior, quantify chargeback exposure, and support faster risk review decisions.
- Developed transaction-level risk features and executive dashboards that translated fraud signals into business metrics including fraud rate, loss concentration, and high-risk segment exposure.
- Designed a GitHub-ready analytics solution with reproducible code, dashboard delivery, and business narrative generation for risk operations and leadership stakeholders.
