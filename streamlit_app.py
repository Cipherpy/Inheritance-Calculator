import streamlit as st

def muslim_inheritance_calculator():
    st.title("Muslim Succession Law Calculator (India)")

    estate = st.number_input("Estate Value (₹)", min_value=0, step=1000)
    deceased_gender = st.radio("Gender of Deceased", ["Male", "Female"])
    marital_status = st.radio("Marital Status", ["Married", "Unmarried"])

    # Spouse details
    spouse_share = 0
    if marital_status == "Married":
        if deceased_gender == "Male":
            wives = st.number_input("Number of wives", min_value=1, max_value=4, step=1)
            spouse_share = (1/8)
        else:
            husband_exists = st.checkbox("Surviving Husband")
            spouse_share = (1/4 if husband_exists else 0)

    # Children details
    num_sons = st.number_input("Number of sons", min_value=0, step=1)
    num_daughters = st.number_input("Number of daughters", min_value=0, step=1)

    # Sibling details
    num_brothers = st.number_input("Number of brothers", min_value=0, step=1)
    num_sisters = st.number_input("Number of sisters", min_value=0, step=1)

    if st.button("Calculate Shares"):
        shares = {}

        spouse_total_share = spouse_share * estate
        remaining_estate = estate - spouse_total_share

        total_children = num_sons + num_daughters

        if total_children > 0:
            units = num_sons * 2 + num_daughters
            unit_share = remaining_estate / units

            if num_sons > 0:
                shares['Each Son'] = unit_share * 2
            if num_daughters > 0:
                shares['Each Daughter'] = unit_share
        elif num_brothers + num_sisters > 0:
            sibling_units = num_brothers * 2 + num_sisters
            sibling_unit_share = remaining_estate / sibling_units

            if num_brothers > 0:
                shares['Each Brother'] = sibling_unit_share * 2
            if num_sisters > 0:
                shares['Each Sister'] = sibling_unit_share
        else:
            shares['Remaining Estate'] = remaining_estate

        if marital_status == "Married":
            if deceased_gender == "Male":
                shares['Each Wife'] = spouse_total_share / wives
            else:
                shares['Husband'] = spouse_total_share

        st.subheader("Inheritance Shares")
        for heir, amount in shares.items():
            st.write(f"{heir}: ₹{amount:,.2f}")

if __name__ == "__main__":
    muslim_inheritance_calculator()
