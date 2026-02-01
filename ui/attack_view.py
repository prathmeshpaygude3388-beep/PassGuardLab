import streamlit as st

def render_attack_view(attack_report: dict):
    st.subheader("⚔️ Attack Intelligence")

    st.metric(
        "Highest Risk Attack",
        attack_report["highest_risk_attack"]
    )

    st.markdown("### Ranked Attacks")

    for attack in attack_report["ranked_attacks"]:
        with st.expander(attack["attack"]):
            st.write(f"**Risk Score:** {attack['risk_score']}")
            st.write(f"**Confidence:** {attack['confidence']}")
            st.json(attack["details"])
            st.info(attack["recommendation"])
