def analyze_risk_trend(previous_scores: list, current_score: float) -> dict:
    """
    Analyzes whether password security posture is improving or degrading.
    """

    if not previous_scores:
        return {
            "trend": "No historical data",
            "change": 0,
            "analysis": "Baseline established"
        }

    avg_previous = sum(previous_scores) / len(previous_scores)
    change = round(current_score - avg_previous, 3)

    if change > 0.05:
        trend = "Improving"
    elif change < -0.05:
        trend = "Degrading"
    else:
        trend = "Stable"

    return {
        "trend": trend,
        "change": change,
        "analysis": (
            "Security posture improving"
            if trend == "Improving"
            else "Security posture worsening"
            if trend == "Degrading"
            else "No significant change"
        )
    }
