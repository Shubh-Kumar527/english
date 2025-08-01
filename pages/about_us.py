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
        <h1 style='color: #2c3e50;'>🎨 know about the developers</h1>
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
elif selected_path == "pages/students_creation.py":
        st.switch_page("pages/students_creation.py")
elif selected_path == "pages/About_the_authers.py":
        st.switch_page("pages/About_the_authers.py")
elif selected_path == "pages/game.py":
    st.switch_page("pages/game.py")
elif selected_path == "pages/about_us.py":
    st.switch_page("pages/about_us.py")
elif selected_path == "pages/school_mag.py":
    st.switch_page("pages/school_mag.py")


# shubh = Image.open("path/to/image.jpg")
afeefa = Image.open("images/afeefa.jpg")
shubh = Image.open("images/shubh3.jpg")


# st.image(image, caption="Optional caption", use_column_width=True)
# st.image(image, caption="Optional caption", use_column_width=True)

d1, d2 = st.columns(2)

with d1:
    desired_height = 300
    aspect_ratio = afeefa.width / afeefa.height
    new_width = int(desired_height * aspect_ratio)
    
    resized_img_afeefa = afeefa.resize((new_width, desired_height))
    st.image(resized_img_afeefa)
    st.write('Name : Afeefa Ansari')
    st.write('class : IX A')
    

with d2:
    desired_height = 300
    aspect_ratio = shubh.width / shubh.height
    new_width = int(desired_height * aspect_ratio)
    
    resized_img_shubh = shubh.resize((new_width, desired_height))
    st.image(resized_img_shubh)
    st.write('Name : Shubh Kumar')
    st.write('class : IX A')

