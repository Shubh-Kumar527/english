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

st.markdown("---")

# Navigation bar
# Set wide layout
st.set_page_config(layout="wide")

# Navigation menu dictionary
menu = {
    "About Authors": "pages/About_the_authers.py",
    "Students Creation": "pages/students_creation.py",
    "School Magazine": "chf",
    "Game": "yigj",
    "About Us": "about-us"
}

# Create columns for nav buttons
cols = st.columns(len(menu))

# Track selected path
selected_path = None

# Render buttons and capture selected path
for i, (label, path) in enumerate(menu.items()):
    if cols[i].button(label):
        selected_path = path

# Divider
st.markdown("---")

# Content logic based on selected path

if selected_path == "pages/About_the_authers.py":
    st.switch_page("pages/About_the_authers.py")
elif selected_path == "pages/students_creation.py":
        st.switch_page("pages/students_creation.py")
elif selected_path == "contact-page":
    pass



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
