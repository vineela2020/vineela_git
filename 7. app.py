import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Loan Risk Prediction System",
    page_icon="💳",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    .main {
        background-color: #F4F6F9;
    }

    .stButton>button {
        background-color: #4B0082;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #6A0DAD;
    }

    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR LOGIN ----------------
st.sidebar.title("🔐 Secure Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if username != "Vineela_shetty" or password != "Vinni@123":
    st.sidebar.warning("Please login to continue")
    st.stop()

# ---------------- TITLE ----------------
st.title("💳 AI Loan Risk Prediction System")
st.markdown("### Professional Banking & Credit Risk Analysis Platform")

)
