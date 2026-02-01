HASH_PROFILES = {
    "md5": {
        "risk": 0.9,
        "description": "Cryptographically broken"
    },
    "sha1": {
        "risk": 0.7,
        "description": "Deprecated and vulnerable"
    },
    "sha256": {
        "risk": 0.4,
        "description": "Strong but fast (not ideal alone)"
    },
    "bcrypt": {
        "risk": 0.15,
        "description": "Adaptive and secure"
    },
    "argon2": {
        "risk": 0.05,
        "description": "Modern and memory-hard"
    }
}


def analyze_hashing_algorithm(algorithm: str) -> dict:
    algo = algorithm.lower()

    profile = HASH_PROFILES.get(
        algo,
        {
            "risk": 0.6,
            "description": "Unknown or custom algorithm"
        }
    )

    return {
        "hash_algorithm": algo,
        "risk_score": profile["risk"],
        "assessment": profile["description"],
        "recommendation": (
            "Use Argon2 or bcrypt with high cost factor"
            if profile["risk"] > 0.3
            else "Hashing strategy is acceptable"
        )
    }
