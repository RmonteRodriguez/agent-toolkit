import math
import streamlit as st

st.title("Renters Billing Calculator")
st.info("Alawys double check final numbers before providing to customer.")

annualPremium = st.number_input("Enter Annual Premium Amount", min_value=0.0, step=1.00)
paymentPlan = st.selectbox(
    "Select Payment Plan",
    ["2 pay", "4 pay"]
)
stateSelect = st.selectbox(
    "Select Policy State",
    ["CA", "CT", "OH", "DC", "LA", "MS", "NC", "WV", "All Other States"]
)

# (upper limit inclusive, fee)
feeTiers = {
    "DC": [(499, 4.00), (649, 5.00), (799, 6.00), (float("inf"), 7.00)],
    "LA": [(499, 4.00), (649, 5.00), (float("inf"), 6.00)],
    "MS": [(499, 4.00), (649, 5.00), (799, 6.00), (949, 7.00), (float("inf"), 8.00)],
    "All Other States": [(499, 4.00), (649, 5.00), (799, 6.00), (949, 7.00), (1099, 8.00)],
}

flatFeeStates = {
    "CA": 6.00, "CT": 6.00, "OH": 6.00, "NC": 3.00, "WV": 3.00,
}

if st.button("Calculate"):
    if annualPremium <= 0:
        st.warning("Enter a premium amount first")
        st.stop()

    if paymentPlan == "2 pay":
        downPayment = annualPremium * 0.55
        installmentBeforeFee = annualPremium * 0.45
        numInstallments = 1
    else:
        downPayment = annualPremium * 0.31
        installmentBeforeFee = annualPremium * 0.23
        numInstallments = 3

    if stateSelect in flatFeeStates:
        installmentFee = flatFeeStates[stateSelect]
    elif stateSelect == "All Other States" and annualPremium >= 1100:
        extra = math.ceil((annualPremium - 1100) / 150)
        installmentFee = 8.00 + extra
    else:
        for limit, fee in feeTiers[stateSelect]:
            if annualPremium <= limit:
                installmentFee = fee
                break

    installmentAmount = installmentBeforeFee + installmentFee
    totalCost = downPayment + numInstallments * installmentAmount
    plural = "payment" if numInstallments == 1 else "payments"

    st.success(f"Down payment of \\${downPayment:,.2f} today, "
               f"then {numInstallments} {plural} of \\${installmentAmount:,.2f} "
               f"with a total cost of \\${totalCost:,.2f} which includes installment fees")

    with st.expander("See breakdown"):
        st.write(f"Annual premium: \\${annualPremium:,.2f}")
        st.write(f"Down payment: \\${downPayment:,.2f}")
        st.write(f"Installment before fee: \\${installmentBeforeFee:,.2f}")
        st.write(f"Installment fee: \\${installmentFee:,.2f}")
        st.write(f"Total fees: \\${numInstallments * installmentFee:,.2f}")