import streamlit as st
import os
from PIL import Image
import base64

# Page config
st.set_page_config(
    page_title="Lingualith",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Header with logo and title (local image, black background)
logo_path = "images/Logo.jpg"  # Replace with your local path

if os.path.exists(logo_path):
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <div style='display: flex; align-items: center; justify-content: center; background-color: black; padding: 2rem 0; border-radius: 10px;'>
            <img src='data:image/png;base64,{encoded_logo}' style='width: 60px; margin-right: 15px;'>
            <h1 style='color: white; font-size: 3rem;'>Lingualith</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("Logo image not found. Please place it at 'assets/logo.png'")

# Navigation bar
# Set wide layout
st.set_page_config(layout="wide")

# Define menu with labels and internal keys (cleaned of special characters)
menu = {
    "Home": "home",
    "Gallery": "gallery",
    "About Us": "aboutus",
    "Contact Page": "contactpage"
}

# Create columns for buttons
cols = st.columns(len(menu))

# Track selected page key
selected_page = None

# Render nav buttons
for i, (label, page_key) in enumerate(menu.items()):
    if cols[i].button(label):
        selected_page = page_key

# Content based on selected page key
st.markdown("---")
if selected_page == "home":
    st.header("Welcome to the Home Page")
elif selected_page == "gallery":
    st.header("Gallery of Student Creations")
elif selected_page == "aboutus":
    st.header("About Us")
elif selected_page == "contactpage":
    st.header("Contact Page")



st.markdown(
    f"""
    <div style='text-align: center; padding: 2rem;'>
        <h2 style='color: white; font-style: italic;'>“TO BE OR NOT TO BE , THAT IS THE QUESTION”</h2>
        <h2 style='color: white; font-style: italic;'>\t-WILLIAM SHAKESPEARE </h2>
    </div>
    """,
    unsafe_allow_html=True
)



# Load local image from user's system
image_path = "images/home_page_collage.jpg"  # replace with your local path
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning("Background image placeholder not found. Please place it at 'assets/main_visual.jpg'")
