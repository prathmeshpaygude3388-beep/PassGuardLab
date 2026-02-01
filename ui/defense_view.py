import streamlit as st

def render_defense_view(defenses: list, zero_trust: dict):
    st.subheader("🛡️ Defense Recommendations")

    for d in defenses:
        st.write(f"• {d}")

    st.markdown("---")

    st.subheader("🔒 Zero Trust Decision")

    st.metric(
        "Identity Trust Score",
        zero_trust["identity_trust_score"]
    )

    st.write(f"**Decision:** {zero_trust['zero_trust_decision']}")
