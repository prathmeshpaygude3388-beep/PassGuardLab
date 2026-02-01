def generate_defense(score, dict_risk, mutation_risk):
    recommendations = []

    if score < 40:
        recommendations.extend([
            "Enforce strong password policy immediately",
            "Enable MFA for all users",
            "Implement account lockout and rate limiting",
            "Monitor authentication logs aggressively"
        ])

    elif score < 70:
        recommendations.extend([
            "Enable MFA for privileged accounts",
            "Block common and breached passwords",
            "Increase minimum password length"
        ])

    else:
        recommendations.extend([
            "Password policy is acceptable",
            "Maintain MFA and monitoring",
            "Plan transition to passwordless authentication"
        ])

    if dict_risk > 0.5:
        recommendations.append("Disallow dictionary-based passwords")

    if mutation_risk > 0.5:
        recommendations.append(
            "Block predictable substitutions (e.g., @ for a, 1 for i)"
        )

    return recommendations
