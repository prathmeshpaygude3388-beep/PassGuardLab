def calculate_resistance(entropy, brute_time, dict_risk, mutation_risk):
    score = (
        (entropy / 100) * 40 +
        (1 / (1 + brute_time)) * 30 +
        (1 - dict_risk) * 15 +
        (1 - mutation_risk) * 15
    )
    return round(min(score, 100), 2)
