def predict_next_failure(
    overall_risk_score: float,
    highest_risk_attack: str,
    defense_recommendations: list
) -> dict:
    """
    Predicts likely next security failure based on current posture.
    """

    if overall_risk_score > 0.7:
        failure = "Credential compromise"
        timeline = "Immediate (days)"

    elif overall_risk_score > 0.4:
        failure = "Account takeover"
        timeline = "Short-term (weeks)"

    else:
        failure = "Policy erosion"
        timeline = "Long-term (months)"

    if "Enable MFA for all users" not in defense_recommendations:
        failure_vector = "Authentication bypass"
    else:
        failure_vector = "Human-factor exploitation"

    return {
        "predicted_failure_event": failure,
        "likely_attack_vector": highest_risk_attack,
        "failure_vector": failure_vector,
        "estimated_timeline": timeline,
        "reasoning": (
            "Prediction based on risk aggregation, attack dominance, "
            "and absence of mitigating controls"
        )
    }
