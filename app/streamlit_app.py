import streamlit as st
import plotly.express as px
from src.risk_features import load_transactions, build_risk_kpis, build_segment_metrics
from src.anomaly_detection import detect_anomalies
from src.summary import build_risk_summary

st.set_page_config(page_title="Fraud and Revenue Risk Monitor", layout="wide")
st.title("Fraud and Revenue Risk Monitoring Platform")
st.caption("Anomaly detection, chargeback exposure, and operational risk monitoring")

df = load_transactions()
kpis = build_risk_kpis(df)
segments = build_segment_metrics(df)
scored = detect_anomalies(df)
summary = build_risk_summary(kpis, segments)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Fraud rate", f"{kpis['fraud_rate']:.2f}%")
c2.metric("Chargeback loss", f"${kpis['chargeback_loss']:,.0f}")
c3.metric("High-risk volume", f"{kpis['high_risk_volume']:,}")
c4.metric("Avg 24h velocity", f"{kpis['avg_velocity']:.2f}")

st.subheader("Risk summary")
st.warning(summary)

loss_fig = px.bar(segments.head(10), x="merchant_category", y="chargeback_loss", color="channel", barmode="group", title="Chargeback Loss by Segment")
st.plotly_chart(loss_fig, use_container_width=True)

fraud_fig = px.bar(segments.head(10), x="merchant_category", y="fraud_rate", color="channel", barmode="group", title="Fraud Rate by Segment")
st.plotly_chart(fraud_fig, use_container_width=True)

st.subheader("Most anomalous transactions")
show_cols = ["transaction_id", "event_ts", "amount", "merchant_category", "channel", "country_risk", "velocity_24h", "is_fraud", "anomaly_score"]
st.dataframe(scored[show_cols].head(25), use_container_width=True)
