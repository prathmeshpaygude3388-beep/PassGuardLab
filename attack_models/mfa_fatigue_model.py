def mfa_fatigue_attack(mfa_enabled: bool, pushes_per_day: int):
    if not mfa_enabled:
        risk = 0.0
    elif pushes_per_day > 10:
        risk = 0.85
    elif pushes_per_day > 5:
        risk = 0.6
    else:
        risk = 0.2

    return {
        "attack": "MFA Fatigue",
        "risk_score": risk,
        "confidence": 0.9,
        "details": {
            "mfa_enabled": mfa_enabled,
            "pushes_per_day": pushes_per_day
        },
        "recommendation": "Enable number-matching MFA and rate limiting"
    }
