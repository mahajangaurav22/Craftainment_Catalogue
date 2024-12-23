import streamlit as st

# Title for the Handmade Cover Pages
st.title("Premium Combo")

# Description or introductory text (optional)
st.write("Explore our collection of beautifully crafted Premium Combos.")

# Paths to your images
image_paths = [
    "/Users/gauravmahajan/Desktop/catalogue/cover pages/border design.jpg",  # Replace with actual image paths
    "/Users/gauravmahajan/Desktop/catalogue/cover pages/cover2.webp",
    "/Users/gauravmahajan/Desktop/catalogue/cover pages/coverpage.jpg",
    "/Users/gauravmahajan/Desktop/catalogue/cover pages/designer.jpg",
    "/Users/gauravmahajan/Desktop/catalogue/cover pages/designer.jpg",
]

# Number of columns
num_columns = 3

# Create a grid layout for images
for i in range(0, len(image_paths), num_columns):
    cols = st.columns(num_columns)  # Create three columns for the current row
    for j in range(num_columns):
        if i + j < len(image_paths):  # Check if there is an image to display
            with cols[j]:
                st.image(image_paths[i + j], caption=f"Printed Cover Image {i + j + 1}", use_column_width=True)
                