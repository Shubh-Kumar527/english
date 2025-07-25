import streamlit as st
import os
from PIL import Image

# Page config
st.set_page_config(
    page_title="Student Creations",
    page_icon="🎨"
)

# Title and Intro
st.markdown(
    """
    <div style='text-align: center; padding: 1rem; background-color: #e9f5ff; border-radius: 10px;'>
        <h1 style='color: #2c3e50;'>🎨 Student Self composed pomes</h1>
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

# Path to your image folder
IMAGE_FOLDER = "stories"

# Load image files
image_files = sorted([
    os.path.join(IMAGE_FOLDER, f)
    for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
])

# Initialize index in session state
if "page_index" not in st.session_state:
    st.session_state.page_index = 0

# Navigation buttons (above the image)
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ Previous") and st.session_state.page_index > 0:
        st.session_state.page_index -= 1
with col3:
    if st.button("Next ➡️") and st.session_state.page_index < len(image_files) - 1:
        st.session_state.page_index += 1

# Show image in the center
if image_files:
    image_path = image_files[st.session_state.page_index]
    img = Image.open(image_path)

    # Resize to fixed width for portrait layout
    max_width = 350
    aspect_ratio = img.height / img.width
    new_height = int(max_width * aspect_ratio)
    img = img.resize((max_width, new_height))

    # Center image
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{st.image(img, output_format="PNG").data}' width="{max_width}px">
            <p>Page {st.session_state.page_index + 1} of {len(image_files)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("No images found in the folder.")
