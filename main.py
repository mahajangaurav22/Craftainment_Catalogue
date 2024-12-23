import streamlit as st

st.set_page_config(page_title="Catalogue Website", layout="wide")
# Main title of the app
st.title("Catalogue Website")


# Navigation Bar with buttons that switch pages directly
st.write("### Navigation")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Cover Pages"):
        st.session_state.page = "Cover Pages"

with col2:
    if st.button("Designer Sheets"):
        st.session_state.page = "Designer Sheets"

with col3:
    if st.button("Combo Main Pages"):
        st.session_state.page = "Combo Main Pages"

# Handle page navigation based on selection
if 'page' in st.session_state:
    if st.session_state.page == "Cover Pages":
        st.write("### Select a subcategory")
        subcategory = st.radio("", ["Printed", "Handmade"])
        
        if subcategory == "Printed":
            if st.button("Go to Printed Cover Page"):
                print("button clicked")
                st.switch_page("pages/printed_cover.py")
                print("button clikced")  # Ensure this matches the filename without .py
        elif subcategory == "Handmade":
            if st.button("Go to Handmade Cover Page"):
                st.switch_page("pages/handmade_cover.py")  # Ensure this matches the filename without .py

    elif st.session_state.page == "Designer Sheets":
        st.write("### Select a subcategory")
        subcategory = st.radio("", ["Printed", "Border Design", "Crafted Sheets"])
        
        if subcategory == "Printed":
            if st.button("Go to Printed Designer Sheet"):
                st.switch_page("pages/printed_designer.py")  # Ensure this matches the filename without .py
        elif subcategory == "Border Design":
            if st.button("Go to Border Design Sheet"):
                st.switch_page("pages/border_design.py")  # Ensure this matches the filename without .py
        elif subcategory == "Crafted Sheets":
            if st.button("Go to Crafted Sheet"):
                st.switch_page("pages/crafted_sheets.py")  # Ensure this matches the filename without .py

    elif st.session_state.page == "Combo Main Pages":
        st.write("### Select a subcategory")
        subcategory = st.radio("", ["Premium Combo Pack", "3D Starter Combo Pack", "Classic Combo Pack"])
        
        if subcategory == "Premium Combo Pack":
            if st.button("Go to Premium Combo Pack"):
                st.switch_page("pages/premium_combo.py")  # Ensure this matches the filename without .py
        elif subcategory == "3D Starter Combo Pack":
            if st.button("Go to 3D Starter Combo Pack"):
                st.switch_page("pages/starter_combo.py")  # Ensure this matches the filename without .py
        elif subcategory == "Classic Combo Pack":
            if st.button("Go to Classic Combo Pack"):
                st.switch_page("pages/classic_combo.py")  # Ensure this matches the filename without .py

else:
    st.write("Please select a category to get started.")
