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
        <h1 style='color: #2c3e50;'>🎨 Student Creations</h1>
        <p style='color: #34495e;'>Explore original poems, stories, essays, and art made by our talented students.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Path to student work folder
student_work_folder = "student_works"

# Get list of student files
if os.path.exists(student_work_folder):
    files = os.listdir(student_work_folder)
    if files:
        for file in files:
            name, ext = os.path.splitext(file)
            file_path = os.path.join(student_work_folder, file)

            st.markdown("---")
            st.subheader(f"🧑‍🎓 {name.replace('_', ' ').title()}")

            if ext.lower() in [".png", ".jpg", ".jpeg"]:
                img = Image.open(file_path)
                st.image(img, caption=name.replace('_', ' ').title(), width=400)
            elif ext.lower() in [".txt", ".md"]:
                with open(file_path, "r", encoding="utf-8") as f:
                    st.markdown(f"<div style='background-color: #fefefe; padding: 1rem; border-radius: 8px; color: #000;'>{f.read()}</div>", unsafe_allow_html=True)
            else:
                st.info(f"File format for {file} not supported for preview.")
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
