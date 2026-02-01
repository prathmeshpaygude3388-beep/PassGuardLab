MUTATION_RULES = {
    "a": ["@", "4"],
    "i": ["1", "!"],
    "o": ["0"],
    "s": ["$", "5"]
}

def mutation_attack(password: str):
    hits = []

    for char, subs in MUTATION_RULES.items():
        for sub in subs:
            if sub in password:
                hits.append(f"{char}->{sub}")

    risk = min(len(hits) * 0.25, 1.0)

    return {
        "attack": "Mutation Attack",
        "risk_score": round(risk, 2),
        "confidence": 0.85,
        "details": {
            "detected_mutations": hits,
            "rule_count": len(MUTATION_RULES)
        },
        "recommendation": "Block predictable character substitutions"
    }
