COMMON_PASSWORD_DATASET = [
    "password", "admin", "welcome", "qwerty",
    "letmein", "login", "root", "user",
    "password123", "admin123", "welcome123"
]

def dictionary_attack(password: str):
    pwd = password.lower()
    matches = [w for w in COMMON_PASSWORD_DATASET if w in pwd]

    risk = 0.9 if matches else 0.1

    return {
        "attack": "Dictionary Attack",
        "risk_score": risk,
        "confidence": 0.9,
        "details": {
            "matched_words": matches,
            "dataset_size": len(COMMON_PASSWORD_DATASET)
        },
        "recommendation": "Disallow dictionary-based passwords"
    }
