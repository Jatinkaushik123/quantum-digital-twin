import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from simulation import multi_stage_cooling
from utils import apply_custom_style
from sklearn.linear_model import LinearRegression

apply_custom_style()

# Page config
st.set_page_config(page_title="Quantum Digital Twin", layout="wide")

# Title section
st.title("🧊 Quantum Cryogenic Digital Twin")
st.caption("Interactive simulation of multi-stage cooling in quantum systems")

# Sidebar
st.sidebar.title("⚙️ Control Panel")
leak = st.sidebar.slider("Heat Leak", 0.0, 0.05, 0.01)
resolution = st.sidebar.slider("Simulation Resolution", 50, 300, 150)

st.sidebar.markdown("---")
st.sidebar.info("Adjust parameters to observe system stability.")

# Layout (2 columns)
col1, col2 = st.columns([2, 1])

time = np.linspace(0, 100, resolution)
T = multi_stage_cooling(time, leak)

# 🔮 Prediction Model
time_reshaped = time.reshape(-1, 1)

model = LinearRegression()
model.fit(time_reshaped, T)

# Predict future (next 50 time units)
future_time = np.linspace(100, 150, 50).reshape(-1, 1)
future_T = model.predict(future_time)

# Prevent unphysical negative temperatures
future_T = np.maximum(future_T, 0)

# LEFT: Graph
with col1:
    st.subheader("📉 Cooling Curve")

    fig, ax = plt.subplots()

# Current simulation
    ax.plot(time, T, linewidth=2, label="Current")

# Prediction line (future)
    ax.plot(future_time, future_T, linestyle="dashed", label="Predicted")

# Labels
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (K)")
    ax.set_title("Cooling Curve with Prediction")

# Stage highlights
    ax.axvspan(0, 30, alpha=0.1)
    ax.axvspan(30, 70, alpha=0.1)
    ax.axvspan(70, 100, alpha=0.1)

# Legend
    ax.legend()

    st.pyplot(fig)

    st.write("""
             - Stage 1: Rapid cooling (300K → 77K)
             - Stage 2: Controlled cooling (77K → 4K)
             - Stage 3: Ultra cooling (~0K) 
            """)

# RIGHT: Metrics & insights
with col2:
    st.subheader("📊 System Status")

    st.metric("Final Temp", f"{T[-1]:.2f} K")
    st.metric("Max Temp", f"{max(T):.2f} K")

    if T[-1] > 5:
        st.warning("⚠️ System did not reach required cryogenic temperature!")

    if leak > 0.02:
        st.error("⚠️ High heat leak → unstable system")
    else:
        st.success("✅ System stable")
    st.markdown("---")

    st.subheader("🔮 Prediction")

    predicted_final = future_T[-1]

    st.write(f"Predicted Temperature after time: {predicted_final:.2f} K")

    if predicted_final <= 0:
        st.info("System approaching physical lower limit (~0 K)")

    if predicted_final > 5:
        st.error("⚠️ Future instability expected!")
    else:
        st.success("✅ System expected to remain stable")

    st.markdown("---")

    st.subheader("🧠 Insight")
    st.write("""
    Even small heat leaks can disturb cryogenic stability,
    which directly impacts quantum computation accuracy.
    """)
