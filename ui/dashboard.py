import streamlit as st

def render_dashboard(
    resistance_score: float,
    overall_risk: float,
    highest_attack: str,
    maturity: dict,
    compliance: dict
):
    st.subheader("📊 Security Overview Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Resistance Score™", f"{resistance_score}/100")

    with col2:
        st.metric("Overall Risk", overall_risk)

    with col3:
        st.metric("Top Attack Vector", highest_attack)

    st.markdown("---")

    st.subheader("🔐 Password Security Maturity")
    st.write(
        f"**Level {maturity['maturity_level']}** – "
        f"{maturity['maturity_description']}"
    )
    st.info(maturity["recommended_next_step"])

    st.markdown("---")

    st.subheader("📋 Compliance Snapshot")
    for key, value in compliance.items():
        st.write(f"**{key}**: {value}")