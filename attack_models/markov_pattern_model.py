import re

HUMAN_PATTERNS = {
    "name_year": r"[A-Z][a-z]+[0-9]{2,4}",
    "caps_first": r"^[A-Z][a-z0-9]+",
    "digits_end": r"[0-9]+$"
}

def markov_pattern_attack(password: str):
    matches = []

    for name, pattern in HUMAN_PATTERNS.items():
        if re.search(pattern, password):
            matches.append(name)

    risk = min(len(matches) * 0.3, 1)

    return {
        "attack": "Markov Pattern Attack",
        "risk_score": round(risk, 2),
        "confidence": 0.8,
        "details": {
            "matched_patterns": matches,
            "pattern_count": len(HUMAN_PATTERNS)
        },
        "recommendation": "Avoid human-readable password structures"
    }
