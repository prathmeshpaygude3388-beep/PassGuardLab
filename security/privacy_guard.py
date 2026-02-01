def privacy_compliance_check(
    stores_passwords: bool,
    logs_sensitive_data: bool,
    transmits_credentials: bool
) -> dict:
    """
    Ensures platform complies with basic privacy principles.
    """

    violations = []

    if stores_passwords:
        violations.append("Password storage detected")

    if logs_sensitive_data:
        violations.append("Sensitive data logging detected")

    if transmits_credentials:
        violations.append("Credential transmission detected")

    compliant = len(violations) == 0

    return {
        "privacy_compliant": compliant,
        "violations": violations,
        "compliance_status": (
            "Compliant with privacy-by-design principles"
            if compliant
            else "Privacy violations detected"
        )
    }
