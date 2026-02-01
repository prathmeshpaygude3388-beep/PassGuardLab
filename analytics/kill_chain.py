def map_attack_kill_chain(
    highest_risk_attack: str,
    overall_risk_score: float
) -> dict:
    """
    Maps password compromise to downstream attack stages.
    """

    chain = ["Credential Access"]

    if overall_risk_score > 0.3:
        chain.append("Account Takeover")

    if overall_risk_score > 0.5:
        chain.append("Privilege Escalation")

    if overall_risk_score > 0.7:
        chain.append("Lateral Movement")

    if overall_risk_score > 0.85:
        chain.append("Persistence")

    return {
        "initial_vector": highest_risk_attack,
        "kill_chain_stages": chain,
        "final_impact": (
            "Full identity compromise"
            if "Persistence" in chain
            else "Partial compromise"
        )
    }
