import math

def normalize_scores(scores: list) -> list:
    total = sum(scores)
    if total == 0:
        return scores
    return [round(s / total, 4) for s in scores]


def softmax(scores: list) -> list:
    exp_scores = [math.exp(s) for s in scores]
    total = sum(exp_scores)
    return [round(e / total, 4) for e in exp_scores]


def confidence_from_variance(scores: list) -> float:
    if len(scores) < 2:
        return 1.0
    mean = sum(scores) / len(scores)
    variance = sum((s - mean) ** 2 for s in scores) / len(scores)
    return round(min(variance * 2, 1.0), 3)
