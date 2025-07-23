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
st.markdown(
    """
    <style>
    .nav-bar {
        background-color: #f0f0f0;
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
    }
    .nav-bar a {
        color: #333;
        margin: 0 1.5rem;
        font-size: 1.2rem;
        text-decoration: none;
    }
    .nav-bar a:hover {
        text-decoration: underline;
    }
    </style>
    <div class='nav-bar'>
        <a href='/Home'>Home</a>
        <a href='/pages/About_the_authers.py'>Meet the Authors</a>
        <a href='/pages/page2.py'>Student Creations</a>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <div style='text-align: center; padding: 2rem;'>
        <h2 style='color: white; font-style: italic;'>“TO BE OR NOT TO BE , THAT IS THE QUESTION”</h2>
        <h2 style='color: white; font-style: italic;'>\t-WILLIAM SHAKESPEARE </h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Placeholder for user-defined full-screen image (local)
st.markdown(
    """
    <div style='text-align: center; padding-top: 2rem;'>
        <h3 style='color: black;'>Your image will appear here</h3>
        <p style='color: black;'>You can replace the placeholder below with your local image.</p>
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
