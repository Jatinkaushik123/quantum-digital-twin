import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stApp {
            background: linear-gradient(135deg, #0e1117, #1c1f26);
        }
        h1, h2, h3 {
            color: #00f5ff;
        }
        .stSlider > div {
            color: #00f5ff;
        }
        </style>
    """, unsafe_allow_html=True)