import streamlit as st

# Title for the Handmade Cover Pages
st.title("Border Design")

# Description or introductory text (optional)
st.write("Explore our collection of beautifully crafted handmade Sheets.")

image_paths = [
    "cover pages/border design.jpg",  # Replace with actual image paths
    "cover pages/cover2.webp",
    "cover pages/coverpage.jpg",
    "cover pages/designer.jpg",
    "cover pages/designer.jpg",
]

# Number of columns
num_columns = 3

# Create a grid layout for images
for i in range(0, len(image_paths), num_columns):
    cols = st.columns(num_columns)  # Create three columns for the current row
    for j in range(num_columns):
        if i + j < len(image_paths):  # Check if there is an image to display
            with cols[j]:
                st.image(image_paths[i + j], caption=f"Printed Cover Image {i + j + 1}",use_container_width=True)
                