REUSE_PATTERNS = {
    "short_password": 0.8,
    "medium_password": 0.5,
    "long_password": 0.2
}

def credential_stuffing_attack(password: str):
    length = len(password)

    if length < 8:
        risk = REUSE_PATTERNS["short_password"]
    elif length < 12:
        risk = REUSE_PATTERNS["medium_password"]
    else:
        risk = REUSE_PATTERNS["long_password"]

    return {
        "attack": "Credential Stuffing",
        "risk_score": risk,
        "confidence": 0.75,
        "details": {
            "password_length": length,
            "reuse_probability_model": REUSE_PATTERNS
        },
        "recommendation": "Enforce unique passwords and enable MFA"
    }
