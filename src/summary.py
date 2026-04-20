def build_risk_summary(kpis: dict, segment_df) -> str:
    worst = segment_df.iloc[0]
    return (
        f"The observed fraud rate is {kpis['fraud_rate']:.1f}% with total estimated chargeback exposure of ${kpis['chargeback_loss']:,.0f}. "
        f"High-risk country volume stands at {kpis['high_risk_volume']:,} transactions, and the average 24-hour transaction velocity is {kpis['avg_velocity']:.1f}. "
        f"The highest-risk segment is {worst['merchant_category']} via {worst['channel']}, where fraud rate reaches {worst['fraud_rate']:.1f}% and chargeback loss totals ${worst['chargeback_loss']:,.0f}."
    )
