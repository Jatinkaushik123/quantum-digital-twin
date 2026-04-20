import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #020617, #0f172a);
            color: white;
        }

        h1, h2, h3 {
            color: #38bdf8;
        }

        /* Glass effect */
        .glass {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
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