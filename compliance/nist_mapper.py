def map_to_nist_800_63(
    resistance_score: float,
    mfa_enabled: bool,
    hash_algorithm: str
) -> dict:
    """
    Maps password posture to NIST SP 800-63B controls.
    """

    controls = {
        "IA-5": "Authenticator Management",
        "IA-7": "Cryptographic Requirements",
        "IA-2": "Multi-Factor Authentication"
    }

    gaps = []

    if resistance_score < 60:
        gaps.append("IA-5: Weak password policy")

    if hash_algorithm.lower() in ["md5", "sha1"]:
        gaps.append("IA-7: Weak hashing algorithm")

    if not mfa_enabled:
        gaps.append("IA-2: MFA not enforced")

    compliant = len(gaps) == 0

    return {
        "standard": "NIST SP 800-63B",
        "compliant": compliant,
        "mapped_controls": controls,
        "identified_gaps": gaps,
        "compliance_summary": (
            "Compliant with NIST digital identity guidelines"
            if compliant
            else "Gaps detected in NIST identity controls"
        )
    }
