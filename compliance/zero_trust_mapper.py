def map_to_zero_trust(
    identity_trust_score: float,
    device_trusted: bool,
    location_anomaly: bool
) -> dict:
    """
    Evaluates alignment with Zero Trust principles.
    """

    principles = [
        "Never trust, always verify",
        "Continuous authentication",
        "Context-aware access"
    ]

    gaps = []

    if identity_trust_score < 0.6:
        gaps.append("Weak identity trust score")

    if not device_trusted:
        gaps.append("Untrusted device posture")

    if location_anomaly:
        gaps.append("Location-based risk detected")

    aligned = len(gaps) == 0

    return {
        "framework": "Zero Trust Architecture",
        "aligned": aligned,
        "principles": principles,
        "identified_gaps": gaps,
        "alignment_summary": (
            "Aligned with Zero Trust principles"
            if aligned
            else "Zero Trust gaps detected"
        )
    }