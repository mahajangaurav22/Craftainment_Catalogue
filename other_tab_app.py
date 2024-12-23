import streamlit as st

# Main title of the app
st.title("Catalogue Website")

# Navigation Bar with buttons that link to subpages
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
                # Open printed_cover.py in a new tab
                st.markdown('<a href="/pages/printed_cover" target="_blank">Open Printed Cover Page</a>', unsafe_allow_html=True)
        elif subcategory == "Handmade":
            if st.button("Go to Handmade Cover Page"):
                # Open handmade_cover.py in a new tab
                st.markdown('<a href="/pages/handmade_cover" target="_blank">Open Handmade Cover Page</a>', unsafe_allow_html=True)

    elif st.session_state.page == "Designer Sheets":
        st.write("### Select a subcategory")
        subcategory = st.radio("", ["Printed", "Border Design", "Crafted Sheets"])
        
        if subcategory == "Printed":
            if st.button("Go to Printed Designer Sheet"):
                # Open printed_designer.py in a new tab
                st.markdown('<a href="/pages/printed_designer" target="_blank">Open Printed Designer Sheet</a>', unsafe_allow_html=True)
        elif subcategory == "Border Design":
            if st.button("Go to Border Design Sheet"):
                # Open border_design.py in a new tab
                st.markdown('<a href="/pages/border_design" target="_blank">Open Border Design Sheet</a>', unsafe_allow_html=True)
        elif subcategory == "Crafted Sheets":
            if st.button("Go to Crafted Sheet"):
                # Open crafted_sheets.py in a new tab
                st.markdown('<a href="/pages/crafted_sheets" target="_blank">Open Crafted Sheet</a>', unsafe_allow_html=True)

    elif st.session_state.page == "Combo Main Pages":
        st.write("### Select a subcategory")
        subcategory = st.radio("", ["Premium Combo Pack", "3D Starter Combo Pack", "Classic Combo Pack"])
        
        if subcategory == "Premium Combo Pack":
            if st.button("Go to Premium Combo Pack"):
                # Open premium_combo.py in a new tab
                st.markdown('<a href="/pages/premium_combo" target="_blank">Open Premium Combo Pack</a>', unsafe_allow_html=True)
        elif subcategory == "3D Starter Combo Pack":
            if st.button("Go to 3D Starter Combo Pack"):
                # Open starter_combo.py in a new tab
                st.markdown('<a href="/pages/starter_combo" target="_blank">Open 3D Starter Combo Pack</a>', unsafe_allow_html=True)
        elif subcategory == "Classic Combo Pack":
            if st.button("Go to Classic Combo Pack"):
                # Open classic_combo.py in a new tab
                st.markdown('<a href="/pages/classic_combo" target="_blank">Open Classic Combo Pack</a>', unsafe_allow_html=True)

else:
    st.write("Please select a category to get started.")
