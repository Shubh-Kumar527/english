import streamlit as st
import os
from PIL import Image
import base64

# Page config
st.set_page_config(
    page_title="Student Creations",
    page_icon="🎨",
    layout="wide"
)

# Title and Intro
st.markdown(
    """
    <div style='text-align: center; padding: 1rem; background-color: #e9f5ff; border-radius: 10px;'>
        <h1 style='color: #2c3e50;'>🎨 Games</h1>
        <p style='color: #34495e;'>Explore original work made by our talented students.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# Navigation bar
# # Navigation menu dictionary
menu = {
    "Home": "Home.py",
    "Author Avenue": "pages/About_the_authers.py",
    "Bright Minds, Bold Words": "pages/students_creation.py",
    "Brain Battles": "pages/game.py",
    "School magazine" : "pages/school_mag.py",
    "Know About The Developers": "pages/about_us.py"
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
if selected_path == "Home.py":
    st.switch_page("Home.py")
elif selected_path == "pages/About_the_authers.py":
        st.switch_page("pages/About_the_authers.py")
elif selected_path == "pages/students_creation.py":
    st.switch_page("pages/students_creation.py")
elif selected_path == "pages/about_us.py":
    st.switch_page("pages/about_us.py")
elif selected_path == "pages/school_mag.py":
    st.switch_page("pages/school_mag.py")

g1, g2 = st.columns(2)

# Load the image
image1 = Image.open('images/img_11.jpg')

image2 = Image.open('images/img_12.jpg')




with g1:
    st.image(image1, caption='My Image', use_container_width=True)
    if st.button("Spotlight On Success"):
        st.switch_page("pages/game1.py")
with g2:
    st.image(image2, caption='My Image', use_container_width=True)
    if st.button("Literary Exploration "):
        st.switch_page("pages/guess_the_auther_game.py")

