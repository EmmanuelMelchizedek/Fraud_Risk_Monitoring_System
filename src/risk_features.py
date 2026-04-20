import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "transactions.csv"


def load_transactions(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["event_ts"])
    df["hour"] = df["event_ts"].dt.hour
    return df


def build_risk_kpis(df: pd.DataFrame) -> dict:
    return {
        "fraud_rate": round(df["is_fraud"].mean() * 100, 2),
        "chargeback_loss": round(df["chargeback_loss"].sum(), 2),
        "high_risk_volume": int((df["country_risk"] == 3).sum()),
        "avg_velocity": round(df["velocity_24h"].mean(), 2),
    }


def build_segment_metrics(df: pd.DataFrame) -> pd.DataFrame:
    seg = (
        df.groupby(["merchant_category", "channel"], as_index=False)
        .agg(
            transactions=("transaction_id", "count"),
            fraud_rate=("is_fraud", "mean"),
            chargeback_loss=("chargeback_loss", "sum"),
            avg_amount=("amount", "mean"),
        )
    )
    seg["fraud_rate"] = (seg["fraud_rate"] * 100).round(2)
    seg["avg_amount"] = seg["avg_amount"].round(2)
    return seg.sort_values(["fraud_rate", "chargeback_loss"], ascending=False)
