from ai_models.model_utils import softmax, confidence_from_variance


def classify_attack_priority(attack_results: list) -> dict:
    """
    Determines which attack is most likely to succeed first.
    Uses weighted risk + attack characteristics.
    """

    attack_names = []
    raw_scores = []

    for attack in attack_results:
        risk = attack["risk_score"]
        confidence = attack.get("confidence", 0.8)

        # weighted score: risk dominates, confidence stabilizes
        score = (risk * 0.7) + (confidence * 0.3)

        attack_names.append(attack["attack"])
        raw_scores.append(score)

    probabilities = softmax(raw_scores)
    conf_score = confidence_from_variance(probabilities)

    ranked = sorted(
        zip(attack_names, probabilities),
        key=lambda x: x[1],
        reverse=True
    )

    return {
        "predicted_fastest_attack": ranked[0][0],
        "attack_probabilities": {
            name: prob for name, prob in ranked
        },
        "model_confidence": conf_score,
        "explanation": "Ranking based on risk-weighted probabilistic modeling"
    }
