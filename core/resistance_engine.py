def calculate_resistance(entropy, brute_time, dict_risk, mutation_risk):
    """
    Resistance Score™ (0–100)

    Higher is better.
    """

    entropy_score = min(entropy / 100, 1) * 40
    brute_score = (1 / (1 + brute_time)) * 30
    dictionary_score = (1 - dict_risk) * 15
    mutation_score = (1 - mutation_risk) * 15

    total_score = (
        entropy_score +
        brute_score +
        dictionary_score +
        mutation_score
    )

    return round(min(total_score, 100), 2)
