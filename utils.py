import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>

        /* Animated gradient background */
        .stApp {
            background: radial-gradient(circle at 20% 20%, #1e293b, #020617);
            animation: moveBg 12s infinite alternate;
            color: white;
        }

        @keyframes moveBg {
            from { background-position: 0% 0%; }
            to { background-position: 100% 100%; }
        }

        h1, h2, h3 {
            color: #38bdf8;
        }

        /* Header bar */
        .header-bar {
            display: flex;
            justify-content: space-between;
            padding: 10px 20px;
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            margin-bottom: 15px;
        }

        .logo {
            font-size: 22px;
            font-weight: bold;
            color: #38bdf8;
        }

        .team {
            font-size: 14px;
            color: #94a3b8;
        }

        /* Metric styling */
        div[data-testid="stMetric"] {
            background: rgba(30, 41, 59, 0.6);
            padding: 10px;
            border-radius: 12px;
        }

        /* Fade animation */
        .fade-in {
            animation: fadeIn 0.8s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        </style>
    """, unsafe_allow_html=True)