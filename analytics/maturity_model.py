def assess_password_maturity(
    resistance_score: float,
    mfa_enabled: bool,
    hash_algorithm: str
) -> dict:
    """
    Password Security Maturity Model (PSMM™)
    """

    if resistance_score < 40:
        level = 1
        description = "Weak passwords, minimal controls"

    elif resistance_score < 60:
        level = 2
        description = "Basic complexity rules enforced"

    elif resistance_score < 75:
        level = 3
        description = "Strong hashing and lockout policies"

    elif resistance_score < 90:
        level = 4
        description = "MFA and monitoring in place"

    else:
        level = 5
        description = "Passwordless / Zero Trust readiness"

    if not mfa_enabled and level >= 4:
        level -= 1

    if hash_algorithm.lower() in ["md5", "sha1"]:
        level = min(level, 2)

    return {
        "maturity_level": level,
        "maturity_description": description,
        "recommended_next_step": f"Move toward level {min(level + 1, 5)}"
    }
