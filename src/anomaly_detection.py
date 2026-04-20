import pandas as pd
from sklearn.ensemble import IsolationForest

FEATURES = ["amount", "country_risk", "prior_chargebacks", "velocity_24h", "account_age_days", "is_weekend"]


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    model = IsolationForest(contamination=0.04, random_state=42)
    scored = df.copy()
    scored["anomaly_flag"] = model.fit_predict(scored[FEATURES])
    scored["anomaly_score"] = model.decision_function(scored[FEATURES])
    scored["is_anomaly"] = (scored["anomaly_flag"] == -1).astype(int)
    return scored.sort_values("anomaly_score")
