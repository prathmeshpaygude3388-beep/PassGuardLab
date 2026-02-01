def calculate_risk_metrics(
    overall_risk_score: float,
    highest_risk_attack: str,
    user_role: str = "user",
    mfa_enabled: bool = True
) -> dict:
    """
    Calculates impact-oriented security metrics.
    """

    role_multiplier = {
        "user": 1.0,
        "power_user": 1.3,
        "admin": 1.8
    }

    blast_radius = round(
        overall_risk_score * role_multiplier.get(user_role, 1.0),
        3
    )

    exposure = "Low"
    if blast_radius > 0.7:
        exposure = "Critical"
    elif blast_radius > 0.4:
        exposure = "High"
    elif blast_radius > 0.2:
        exposure = "Medium"

    attacker_roi = round(
        blast_radius * (0.7 if mfa_enabled else 1.2),
        3
    )

    return {
        "blast_radius_score": blast_radius,
        "exposure_level": exposure,
        "most_damaging_attack": highest_risk_attack,
        "attacker_roi_index": attacker_roi,
        "impact_summary": (
            "High likelihood of lateral movement and privilege abuse"
            if exposure in ["High", "Critical"]
            else "Contained identity risk"
        )
    }
