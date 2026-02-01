def social_engineering_attack(password: str, username: str = ""):
    signals = []

    if username and username.lower() in password.lower():
        signals.append("username_in_password")

    if len(password) < 8:
        signals.append("short_password")

    risk = min(len(signals) * 0.45, 1)

    return {
        "attack": "Social Engineering",
        "risk_score": round(risk, 2),
        "confidence": 0.7,
        "details": {
            "signals_detected": signals
        },
        "recommendation": "Avoid personal identifiers in passwords"
    }
