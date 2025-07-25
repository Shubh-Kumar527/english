import streamlit as st
import os
from PIL import Image

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
        <h1 style='color: #2c3e50;'>🎨 Student creativity</h1>
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
    "About Authors": "pages/About_the_authers.py",
    "Students Creation": "pages/students_creation.py",
    "Game": "pages/game.py",
    "About Us": "pages/about_us.py"
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
elif selected_path == "pages/game.py":
    st.switch_page("pages/game.py")
elif selected_path == "pages/about_us.py":
    st.switch_page("pages/about_us.py")


# Path to student work folder
student_work_folder = "poems"

# Get list of student files
if os.path.exists(student_work_folder):
    files = os.listdir(student_work_folder)
    if files:
        image_files = [f for f in files if os.path.splitext(f)[1].lower() in [".png", ".jpg", ".jpeg"]]
        text_files = [f for f in files if os.path.splitext(f)[1].lower() in [".txt", ".md"]]

        combined_files = image_files + text_files

        for i in range(0, len(combined_files), 4):
            row = combined_files[i:i+4]
            cols = st.columns(len(row))
            for j, file in enumerate(row):
                with cols[j]:
                    name, ext = os.path.splitext(file)
                    file_path = os.path.join(student_work_folder, file)
                    if ext.lower() in [".png", ".jpg", ".jpeg"]:
                        img = Image.open(file_path)
                        st.image(img, caption=name.replace('_', ' ').title(), width=200)
                    elif ext.lower() in [".txt", ".md"]:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            st.markdown(f"<div style='background-color: #fefefe; padding: 1rem; border-radius: 8px; color: #000;'>"
                                        f"<h4>{name.replace('_', ' ').title()}</h4>"
                                        f"<p>{content}</p></div>", unsafe_allow_html=True)
    else:
        st.info("No student submissions yet. Please check back soon!")
else:
    st.warning(f"Folder '{student_work_folder}' not found. Please ensure it exists with content.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #000;'>"
    "&copy; 2025 English Exhibition. Proudly presenting student creativity."
    "</div>",
    unsafe_allow_html=True
)
