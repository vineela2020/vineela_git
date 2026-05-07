
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

st.markdown("---")

# ---------------- CUSTOMER DETAILS ----------------
st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 18, 80, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced"]
    )

with col2:
    education = st.selectbox(
        "Education",
        ["Graduate", "Post Graduate", "Diploma", "Others"]
    )

    employment_years = st.number_input(
        "Years with Current Employer",
        0,
        40,
        5
    )

    monthly_income = st.number_input(
        "Monthly Income",
        0,
        1000000,
        30000
    )

with col3:
    loan_type = st.selectbox(
        "Loan Type",
        [
            "Personal Loan",
            "Home Loan",
            "Auto Loan",
            "Gold Loan",
            "Credit Card",
            "Consumer Loan"
        ]
    )

    credit_score = st.slider(
        "Credit Score",
        300,
        900,
        650
    )

# ---------------- FINANCIAL BEHAVIOR ----------------
st.markdown("---")
st.subheader("📊 Financial Behavior Analysis")

col4, col5, col6 = st.columns(3)

with col4:
    total_enquiries = st.number_input(
        "Total Credit Enquiries",
        0,
        50,
        2
    )

    delinquency = st.number_input(
        "Number of Delinquencies",
        0,
        20,
        0
    )

with col5:
    missed_payments = st.number_input(
        "Missed Payments",
        0,
        20,
        0
    )

    cc_utilization = st.slider(
        "Credit Card Utilization (%)",
        0,
        100,
        35
    )

with col6:
    active_loans = st.number_input(
        "Active Loans",
        0,
        20,
        1
    )

    debt_ratio = st.slider(
        "Debt Ratio (%)",
        0,
        100,
        30
    )

# ---------------- PREDICTION LOGIC ----------------
st.markdown("---")

if st.button("🔍 Predict Loan Risk"):

    risk_score = 0

    # Credit Score Analysis
    if credit_score < 550:
        risk_score += 40
    elif credit_score < 650:
        risk_score += 25
    else:
        risk_score += 10

    # Income Analysis
    if monthly_income < 20000:
        risk_score += 25
    elif monthly_income < 50000:
        risk_score += 15
    else:
        risk_score += 5

    # Delinquency Analysis
    if delinquency > 5:
        risk_score += 30
    elif delinquency > 2:
        risk_score += 15

    # Missed Payments
    if missed_payments > 5:
        risk_score += 25
    elif missed_payments > 2:
        risk_score += 10

    # Enquiries
    if total_enquiries > 8:
        risk_score += 20
    elif total_enquiries > 4:
        risk_score += 10

    # Utilization
    if cc_utilization > 80:
        risk_score += 20
    elif cc_utilization > 50:
        risk_score += 10

    # Final Category
    if risk_score <= 35:
        category = "🟢 Low Risk"
        recommendation = "Loan can be approved with minimal risk."
        color = "green"

    elif risk_score <= 70:
        category = "🟠 Medium Risk"
        recommendation = "Loan approval requires additional verification."
        color = "orange"

    else:
        category = "🔴 High Risk"
        recommendation = "High probability of loan default risk."
        color = "red"

    # ---------------- RESULTS ----------------
    st.success("Prediction Completed Successfully")

    col7, col8, col9 = st.columns(3)

    with col7:
        st.metric("Risk Score", risk_score)

    with col8:
        st.metric("Risk Category", category)

    with col9:
        st.metric("Credit Score", credit_score)

    st.markdown("---")

    # Risk Gauge
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = risk_score,
        title = {'text': "Risk Score"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 35], 'color': 'lightgreen'},
                {'range': [35, 70], 'color': 'orange'},
                {'range': [70, 100], 'color': 'red'}
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    # ---------------- CUSTOMER PROFILE ----------------
    st.subheader("📌 Customer Risk Summary")

    summary_df = pd.DataFrame({
        "Feature": [
            "Credit Score",
            "Monthly Income",
            "Delinquencies",
            "Missed Payments",
            "Credit Enquiries",
            "CC Utilization"
        ],
        "Value": [
            credit_score,
            monthly_income,
            delinquency,
            missed_payments,
            total_enquiries,
            cc_utilization
        ]
    })

    st.dataframe(summary_df, use_container_width=True)

    # ---------------- INSIGHTS ----------------
    st.subheader("📈 AI Risk Insights")

    insights = []

    if credit_score < 550:
        insights.append("Low credit score indicates repayment risk.")

    if delinquency > 3:
        insights.append("High delinquency history detected.")

    if missed_payments > 2:
        insights.append("Customer has multiple missed payments.")

    if total_enquiries > 5:
        insights.append("Frequent credit enquiries observed.")

    if cc_utilization > 70:
        insights.append("High credit utilization may indicate financial stress.")

    if len(insights) == 0:
        insights.append("Customer financial profile appears stable.")

    for insight in insights:
        st.write("✅", insight)

    # ---------------- RECOMMENDATION ----------------
    st.markdown("---")

    st.subheader("🏦 Loan Approval Recommendation")

    st.info(recommendation)

    # ---------------- CHARTS ----------------
    st.markdown("---")

    st.subheader("📊 Financial Risk Visualization")

    chart_df = pd.DataFrame({
        "Category": [
            "Credit Score",
            "Income",
            "Delinquency",
            "Missed Payments",
            "Enquiries",
            "CC Utilization"
        ],
        "Value": [
            credit_score,
            monthly_income/1000,
            delinquency,
            missed_payments,
            total_enquiries,
            cc_utilization
        ]
    })

    fig2 = px.bar(
        chart_df,
        x="Category",
        y="Value",
        color="Category",
        title="Customer Financial Profile"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ---------------- DOWNLOAD REPORT ----------------
    st.markdown("---")

    report = pd.DataFrame({
        "Customer Details": [
            username,
            age,
            gender,
            monthly_income,
            credit_score,
            risk_score,
            category
        ]
    })

    csv = report.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 Download Risk Report",
        data=csv,
        file_name='loan_risk_report.csv',
        mime='text/csv'
    )

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<center><h5>AI Loan Risk Prediction System | Developed using Streamlit & Python</h5></center>",
    unsafe_allow_html=True
)
