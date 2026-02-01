import streamlit as st

def render_policy_simulator():
    st.subheader("🧪 Policy Simulation Lab")

    mfa = st.checkbox("Enable MFA", value=True)
    trusted_device = st.checkbox("Trusted Device", value=True)
    location_anomaly = st.checkbox("Location Anomaly", value=False)

    return {
        "mfa_enabled": mfa,
        "device_trusted": trusted_device,
        "location_anomaly": location_anomaly
    }
