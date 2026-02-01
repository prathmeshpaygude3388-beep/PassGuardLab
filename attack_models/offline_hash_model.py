HASH_STRENGTH = {
    "md5": 0.9,
    "sha1": 0.7,
    "sha256": 0.4,
    "bcrypt": 0.15,
    "argon2": 0.05
}

def offline_hash_attack(hash_algo: str):
    risk = HASH_STRENGTH.get(hash_algo.lower(), 0.6)

    return {
        "attack": "Offline Hash Attack",
        "risk_score": risk,
        "confidence": 0.95,
        "details": {
            "hash_algorithm": hash_algo,
            "hash_risk_map": HASH_STRENGTH
        },
        "recommendation": "Use bcrypt or Argon2 with high cost factor"
    }
