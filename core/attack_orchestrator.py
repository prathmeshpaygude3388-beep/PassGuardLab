from attack_models.brute_force_model import estimate_bruteforce
from attack_models.dictionary_model import dictionary_attack
from attack_models.mutation_model import mutation_attack
from attack_models.credential_stuffing_model import credential_stuffing_attack
from attack_models.password_spraying_model import password_spraying_attack
from attack_models.markov_pattern_model import markov_pattern_attack
from attack_models.offline_hash_model import offline_hash_attack
from attack_models.social_engineering_model import social_engineering_attack
from attack_models.mfa_fatigue_model import mfa_fatigue_attack


def run_all_attack_simulations(
    password: str,
    features: dict,
    username: str = "",
    hash_algorithm: str = "bcrypt",
    mfa_enabled: bool = True,
    mfa_pushes_per_day: int = 3
) -> dict:
    """
    Central orchestration engine for PASSGUARD LABS

    Returns a structured attack intelligence report:
    - individual attack outputs
    - ranked attack priority
    - overall risk score
    """

    attack_results = []

    # -------------------------------
    # Brute Force
    # -------------------------------
    attack_results.append(
        estimate_bruteforce(
            password_length=features["length"],
            entropy=features["entropy"]
        )
    )

    # -------------------------------
    # Dictionary Attack
    # -------------------------------
    attack_results.append(
        dictionary_attack(password)
    )

    # -------------------------------
    # Mutation Attack
    # -------------------------------
    attack_results.append(
        mutation_attack(password)
    )

    # -------------------------------
    # Credential Stuffing
    # -------------------------------
    attack_results.append(
        credential_stuffing_attack(password)
    )

    # -------------------------------
    # Password Spraying
    # -------------------------------
    attack_results.append(
        password_spraying_attack(password)
    )

    # -------------------------------
    # Markov Pattern Attack
    # -------------------------------
    attack_results.append(
        markov_pattern_attack(password)
    )

    # -------------------------------
    # Offline Hash Attack
    # -------------------------------
    attack_results.append(
        offline_hash_attack(hash_algorithm)
    )

    # -------------------------------
    # Social Engineering
    # -------------------------------
    attack_results.append(
        social_engineering_attack(password, username)
    )

    # -------------------------------
    # MFA Fatigue
    # -------------------------------
    attack_results.append(
        mfa_fatigue_attack(mfa_enabled, mfa_pushes_per_day)
    )

    # -------------------------------
    # Normalize & Rank Attacks
    # -------------------------------
    ranked_attacks = sorted(
        attack_results,
        key=lambda x: x["risk_score"],
        reverse=True
    )

    # -------------------------------
    # Overall Risk Calculation
    # -------------------------------
    overall_risk = round(
        sum(a["risk_score"] for a in attack_results) / len(attack_results),
        3
    )

    # -------------------------------
    # Final Platform Output
    # -------------------------------
    return {
        "overall_risk_score": overall_risk,
        "attack_count": len(attack_results),
        "highest_risk_attack": ranked
