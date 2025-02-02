import streamlit as st

st.set_page_config(page_title="Income Tax Calculator", page_icon="💰", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #1e1e1e;
        }
        .main {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            color: #ffcc00;
            text-align: center;
        }
        .tax-box {
            background-color: black;
            color: white;
            padding: 10px;
            border-radius: 8px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
        }
        .breakdown-box {
            background-color: #2e2e2e;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

def calculate_tax(income):
    taxable_income = income - 75000  
    tax = 0
    actual_tax = 0

    if taxable_income > 0:
        if taxable_income <= 400000:
            tax = 0
        elif taxable_income <= 800000:
            tax = (taxable_income - 400000) * 0.05
        elif taxable_income <= 1200000:
            tax = (400000 * 0.05) + (taxable_income - 800000) * 0.10
        elif taxable_income <= 1600000:
            tax = (400000 * 0.05) + (400000 * 0.10) + (taxable_income - 1200000) * 0.15
        elif taxable_income <= 2000000:
            tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (taxable_income - 1600000) * 0.20
        elif taxable_income <= 2400000:
            tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (taxable_income - 2000000) * 0.25
        else:
            tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (400000 * 0.25) + (taxable_income - 2400000) * 0.30

        if taxable_income <= 1200000:
            tax = max(0, tax - 60000)

        actual_tax = tax

    return actual_tax

st.title("💰 Income Tax Calculator (2025-26)")

with st.expander("ℹ️ Tax Information"):
    st.markdown("""
    - **A Standard Deduction of ₹75,000** is provided to all salaried individuals.
    - **The 87A Rebate of ₹60,000** is applicable **only if taxable income is below ₹12 Lakhs**.
    - Tax slabs vary based on income levels.
    """)

input_method = st.radio("Choose your income input method:", ["Use Slider", "Enter Manually"], index=0)

if input_method == "Use Slider":
    income = st.slider("Select your annual income (₹):", min_value=0, max_value=5000000, step=1, value=500000)
    manual_income = None
else:
    manual_income = st.number_input("Enter your annual income (₹):", min_value=0, step=1000, value=500000)
    income = None

final_income = manual_income if manual_income is not None else income

tax_amount = calculate_tax(final_income)

st.markdown(f"""
    <div class="tax-box">
        📌 Your calculated tax: ₹{tax_amount:,.2f}
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="breakdown-box">
        📝 Tax Breakdown:
        <br> - Standard Deduction: ₹75,000
        <br> - Taxable Income: ₹{final_income - 75000:,.2f}
    </div>
""", unsafe_allow_html=True)
