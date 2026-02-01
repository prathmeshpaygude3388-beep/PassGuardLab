import streamlit as st

# =========================
# Core imports
# =========================
from core.feature_extractor import extract_features
from core.resistance_engine import calculate_resistance
from core.attack_orchestrator import run_all_attack_simulations
from core.defense_engine import generate_defense

# =========================
# AI imports
# =========================
from ai_models.attack_classifier import classify_attack_priority
from ai_models.failure_predictor import predict_next_failure

# =========================
# Analytics imports
# =========================
from analytics.risk_metrics import calculate_risk_metrics
from analytics.kill_chain import map_attack_kill_chain
from analytics.maturity_model import assess_password_maturity
from analytics.trend_analysis import analyze_risk_trend

# =========================
# Security imports
# =========================
from security.zero_knowledge import sanitize_password, destroy_password
from security.zero_trust import zero_trust_assessment
from security.hashing import analyze_hashing_algorithm

# =========================
# Compliance imports
# =========================
from compliance.nist_mapper import map_to_nist_800_63
from compliance.iso27001_mapper import map_to_iso27001
from compliance.zero_trust_mapper import map_to_zero_trust

# =========================
# UI imports
# =========================
from ui.dashboard import render_dashboard
from ui.attack_view import render_attack_view
from ui.defense_view import render_defense_view
from ui.policy_simulator import render_policy_simulator


# =========================
# Streamlit config
# =========================
st.set_page_config(
    page_title="PASSGUARD LABS",
    layout="wide"
)

st.title("🔐 PASSGUARD LABS")
st.caption(
    "Identity Security Platform • Attack Simulation • AI Risk Analytics"
)

st.markdown("---")


# =========================
# Sidebar controls
# =========================
st.sidebar.header("Analysis Controls")

analysis_mode = st.sidebar.radio(
    "Select View",
    [
        "Executive Dashboard",
        "Attack Intelligence",
        "Defense & Zero Trust",
        "Compliance & Standards"
    ]
)

hash_algorithm = st.sidebar.selectbox(
    "Password Hashing Algorithm",
    ["bcrypt", "argon2", "sha256", "sha1", "md5"]
)

username = st.sidebar.text_input(
    "Username (optional)",
    value=""
)

previous_scores = st.sidebar.text_area(
    "Previous Resistance Scores (comma-separated)",
    value=""
)

st.sidebar.markdown("---")
st.sidebar.caption("All analysis is analytical & zero-knowledge.")


# =========================
# Main input
# =========================
password = st.text_input(
    "Enter password for analysis",
    type="password"
)

run = st.button("Run Full Analysis")


# =========================
# Main execution
# =========================
if run and password:

    # -------- Zero Knowledge --------
    pwd = sanitize_password(password)

    # -------- Feature Extraction --------
    features = extract_features(pwd)

    # -------- Attack Orchestration --------
    attack_report = run_all_attack_simulations(
        password=pwd,
        features=features,
        username=username,
        hash_algorithm=hash_algorithm,
        mfa_enabled=True,
        mfa_pushes_per_day=3
    )

    # -------- Resistance Score --------
    resistance_score = calculate_resistance(
        entropy=features["entropy"],
        brute_time=attack_report["raw_attack_data"][0]["details"]["estimated_time_seconds"]["medium"],
        dict_risk=next(a["risk_score"] for a in attack_report["raw_attack_data"] if a["attack"] == "Dictionary Attack"),
        mutation_risk=next(a["risk_score"] for a in attack_report["raw_attack_data"] if a["attack"] == "Mutation Attack")
    )

    # -------- Defense Engine --------
    defenses = generate_defense(
        resistance_score,
        dict_risk=next(a["risk_score"] for a in attack_report["raw_attack_data"] if a["attack"] == "Dictionary Attack"),
        mutation_risk=next(a["risk_score"] for a in attack_report["raw_attack_data"] if a["attack"] == "Mutation Attack")
    )

    # -------- AI Layer --------
    attack_ai = classify_attack_priority(
        attack_report["raw_attack_data"]
    )

    failure_ai = predict_next_failure(
        overall_risk_score=attack_report["overall_risk_score"],
        highest_risk_attack=attack_report["highest_risk_attack"],
        defense_recommendations=defenses
    )

    # -------- Analytics --------
    maturity = assess_password_maturity(
        resistance_score,
        mfa_enabled=True,
        hash_algorithm=hash_algorithm
    )

    risk_metrics = calculate_risk_metrics(
        attack_report["overall_risk_score"],
        attack_report["highest_risk_attack"],
        user_role="user",
        mfa_enabled=True
    )

    kill_chain = map_attack_kill_chain(
        attack_report["highest_risk_attack"],
        attack_report["overall_risk_score"]
    )

    prev_scores = [
        float(x.strip())
        for x in previous_scores.split(",")
        if x.strip().isdigit()
    ]

    trend = analyze_risk_trend(
        prev_scores,
        resistance_score
    )

    # -------- Security --------
    zero_trust = zero_trust_assessment(
        resistance_score,
        mfa_enabled=True,
        device_trusted=True,
        location_anomaly=False
    )

    hashing = analyze_hashing_algorithm(hash_algorithm)

    # -------- Compliance --------
    nist = map_to_nist_800_63(
        resistance_score,
        mfa_enabled=True,
        hash_algorithm=hash_algorithm
    )

    iso = map_to_iso27001(
        resistance_score,
        mfa_enabled=True
    )

    zt = map_to_zero_trust(
        zero_trust["identity_trust_score"],
        device_trusted=True,
        location_anomaly=False
    )

    # -------- Destroy Password --------
    destroy_password(pwd)

    # =========================
    # UI Rendering
    # =========================
    if analysis_mode == "Executive Dashboard":
        render_dashboard(
            resistance_score,
            attack_report["overall_risk_score"],
            attack_report["highest_risk_attack"],
            maturity,
            {
                "NIST": nist["compliance_summary"],
                "ISO 27001": iso["compliance_summary"],
                "Zero Trust": zt["alignment_summary"]
            }
        )

        st.markdown("### 📈 Risk Trend")
        st.json(trend)

    elif analysis_mode == "Attack Intelligence":
        render_attack_view(attack_report)
        st.markdown("### 🤖 AI Attack Prediction")
        st.json(attack_ai)

        st.markdown("### 🔮 Failure Forecast")
        st.json(failure_ai)

    elif analysis_mode == "Defense & Zero Trust":
        render_defense_view(defenses, zero_trust)
        st.markdown("### 🔗 Kill Chain Impact")
        st.json(kill_chain)

    elif analysis_mode == "Compliance & Standards":
        st.subheader("📜 Compliance Mapping")
        st.json(nist)
        st.json(iso)
        st.json(zt)


# =========================
# Footer
# =========================
st.markdown("---")
st.caption(
    "PASSGUARD LABS is a defensive identity security research platform. "
    "No credentials are stored, logged, or transmitted."
)
