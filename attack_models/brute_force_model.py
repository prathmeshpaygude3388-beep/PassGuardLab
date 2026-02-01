ATTACKER_PROFILES = {
    "low": 1e6,       # guesses/sec
    "medium": 1e8,
    "high": 1e10
}

def estimate_bruteforce(password_length: int, entropy: float):
    results = {}

    for level, gps in ATTACKER_PROFILES.items():
        time_seconds = (2 ** entropy) / gps
        results[level] = round(time_seconds, 2)

    risk = 1 / (1 + results["medium"])

    return {
        "attack": "Brute Force",
        "risk_score": round(min(risk, 1), 3),
        "confidence": 0.95,
        "details": {
            "entropy": entropy,
            "estimated_time_seconds": results,
            "password_length": password_length
        },
        "recommendation": "Increase password length and character diversity"
    }
