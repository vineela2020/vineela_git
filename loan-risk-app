import streamlit as st

# ---------------- LOGIN SYSTEM ----------------
st.sidebar.title("Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if username != "Vineela_shetty" or password != "Vinni@123":
    st.warning("Please login to continue")
    st.stop()

# ---------------- MAIN APP ----------------
st.title("Loan Risk Prediction App")

st.write("Enter customer details below:")

# Inputs
credit_score = st.number_input("Credit Score", min_value=300, max_value=900)
income = st.number_input("Monthly Income")

delinquency = st.number_input("Number of Delinquencies", min_value=0)

# Prediction logic
if st.button("Predict Risk"):

    if credit_score < 600 or delinquency > 2:
        st.error("🔴 High Risk Customer")
    elif credit_score < 700:
        st.warning("🟡 Medium Risk Customer")
    else:
        st.success("🟢 Low Risk Customer")

