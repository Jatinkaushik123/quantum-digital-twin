import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from simulation import multi_stage_cooling
from utils import apply_custom_style
from sklearn.linear_model import LinearRegression
import time as t

# Page config
st.set_page_config(page_title="Quantum Digital Twin", layout="wide")

# Apply UI styling
apply_custom_style()

# =========================
# 🚀 TEAM LOADING SCREEN
# =========================
if "loaded" not in st.session_state:
    st.session_state.loaded = False

loading_placeholder = st.empty()

if not st.session_state.loaded:
    with loading_placeholder.container():

        st.markdown("""
        <h2 style='text-align: center; color: #38bdf8;'>
        🚀 Welcome to our Team Project
        </h2>
        <h3 style='text-align: center;'>
        Digital Twin of a Quantum Cryogenic System
        </h3>
        <p style='text-align: center; font-size:18px;'>
        👨‍💻 Developed by <b>Jatin, Sakshi, Simran, Nikita</b>
        </p>
        """, unsafe_allow_html=True)

        st.markdown("---")

        status = st.empty()
        messages = [
            "Initializing Cryogenic Layers...",
            "Stabilizing Quantum Environment...",
            "Loading Digital Twin Model...",
            "Finalizing System..."
        ]

        for msg in messages:
            status.markdown(f"### ⚙️ {msg}")
            t.sleep(0.4)

        progress = st.progress(0)
        for i in range(100):
            t.sleep(0.01)
            progress.progress(i + 1)

    st.session_state.loaded = True
    loading_placeholder.empty()

# =========================
# ✨ FADE-IN START
# =========================
st.markdown('<div class="fade-in">', unsafe_allow_html=True)

# Title
st.title("🧊 Quantum Cryogenic Digital Twin")
st.caption("Interactive simulation of cryogenic cooling in quantum systems")

# Sidebar
st.sidebar.title("⚙️ Control Panel")
leak = st.sidebar.slider("Heat Leak", 0.0, 0.05, 0.01)
resolution = st.sidebar.slider("Simulation Resolution (Data Points)", 50, 300, 150)

st.sidebar.markdown("---")
st.sidebar.info("Adjust parameters to observe system stability.")

# Layout
col1, col2 = st.columns([2, 1])

# Data
time = np.linspace(0, 100, resolution)
T = multi_stage_cooling(time, leak)

# Prediction
model = LinearRegression()
model.fit(time.reshape(-1, 1), T)

future_time = np.linspace(100, 150, 50).reshape(-1, 1)
future_T = model.predict(future_time)
future_T = np.maximum(future_T, 0)

# =========================
# 📉 GRAPH
# =========================
with col1:
    st.subheader("📉 Cooling Curve")

    fig, ax = plt.subplots()
    placeholder = st.empty()

    steps = np.linspace(10, len(time), 80).astype(int)

    for i in steps:
        ax.clear()

        ax.plot(time[:i], T[:i], linewidth=2.5, color="#38bdf8", label="Current")

        if i > len(time)//2:
            ax.plot(future_time, future_T, linestyle="dashed", color="#f59e0b", label="Predicted")

        ax.set_xlabel("Time", color="white")
        ax.set_ylabel("Temperature (K)", color="white")
        ax.set_title("Real-Time Cooling Simulation", color="white")

        ax.tick_params(colors='white')
        ax.set_facecolor("#020617")
        fig.patch.set_facecolor("#020617")

        ax.legend()
        ax.grid(alpha=0.2)

        placeholder.pyplot(fig)
        t.sleep(0.01)

    st.markdown("---")

    st.subheader("🧊 Cooling Stages")
    st.write("""
    - Stage 1: Rapid cooling (300K → 77K)
    - Stage 2: Controlled cooling (77K → 4K)
    - Stage 3: Ultra cooling (~0K)
    """)

# =========================
# 📊 RIGHT PANEL
# =========================
with col2:
    st.subheader("🌡 Live Temperature")
    st.metric("Current Temperature", f"{T[-1]:.2f} K")

    progress_val = int((300 - T[-1]) / 300 * 100)
    progress_val = max(0, min(progress_val, 100))

    st.subheader("📊 Cooling Progress")
    st.progress(progress_val)
    st.write(f"{progress_val}% cooled")

    st.markdown("---")

    st.subheader("📊 System Status")
    st.metric("Final Temp", f"{T[-1]:.2f} K")
    st.metric("Max Temp", f"{max(T):.2f} K")

    if leak > 0.02:
        st.error("⚠️ High heat leak → unstable system")
    else:
        st.success("✅ System stable")

    st.markdown("---")

    st.subheader("🔮 Prediction")
    pred = future_T[-1]

    st.write(f"Predicted Temperature: {pred:.2f} K")

    if pred <= 0:
        st.info("System approaching physical lower limit (~0 K)")
    elif pred > 5:
        st.error("⚠️ Future instability expected!")
    else:
        st.success("✅ System expected to remain stable")

    st.markdown("---")

    st.subheader("🧠 Insight")
    st.info("Small temperature fluctuations can destabilize qubits.")

# =========================
# ✨ FADE-IN END
# =========================
st.markdown('</div>', unsafe_allow_html=True)