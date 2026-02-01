def map_to_iso27001(
    resistance_score: float,
    mfa_enabled: bool,
    monitoring_enabled: bool = True
) -> dict:
    """
    Maps identity security posture to ISO/IEC 27001 Annex A controls.
    """

    controls = {
        "A.9.2": "User access management",
        "A.9.4": "System and application access control",
        "A.12.4": "Logging and monitoring"
    }

    gaps = []

    if resistance_score < 65:
        gaps.append("A.9.4: Weak authentication mechanisms")

    if not mfa_enabled:
        gaps.append("A.9.2: MFA not implemented")

    if not monitoring_enabled:
        gaps.append("A.12.4: Insufficient logging and monitoring")

    compliant = len(gaps) == 0

    return {
        "standard": "ISO/IEC 27001",
        "compliant": compliant,
        "mapped_controls": controls,
        "identified_gaps": gaps,
        "compliance_summary": (
            "ISO 27001 access control requirements satisfied"
            if compliant
            else "ISO 27001 access control gaps identified"
        )
    }
