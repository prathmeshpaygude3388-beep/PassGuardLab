def predict_fastest_attack(attack_results: dict) -> str:
    """
    Predicts the most likely successful attack
    based on risk and time estimates.
    """

    scores = {
        "brute_force": 1 / (1 + attack_results["brute_force_time"]),
        "dictionary": attack_results["dictionary_risk"],
        "mutation": attack_results["mutation_risk"],
    }

    return max(scores, key=scores.get)
