def zero_trust_assessment(
    resistance_score: float,
    mfa_enabled: bool,
    device_trusted: bool,
    location_anomaly: bool
) -> dict:
    """
    Computes an Identity Trust Score based on Zero Trust principles.
    """

    trust_score = resistance_score / 100

    if mfa_enabled:
        trust_score += 0.2
    else:
        trust_score -= 0.2

    if not device_trusted:
        trust_score -= 0.15

    if location_anomaly:
        trust_score -= 0.2

    trust_score = max(min(trust_score, 1.0), 0.0)

    trust_level = "Low"
    if trust_score > 0.75:
        trust_level = "High"
    elif trust_score > 0.45:
        trust_level = "Medium"

    return {
        "identity_trust_score": round(trust_score, 3),
        "trust_level": trust_level,
        "zero_trust_decision": (
            "Allow access"
            if trust_level == "High"
            else "Step-up authentication required"
            if trust_level == "Medium"
            else "Access denied"
        )
    }
