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

# Set the folder path where student work images are stored
IMAGE_FOLDER = "stories"

# Load image paths
image_files = sorted([
    os.path.join(IMAGE_FOLDER, file)
    for file in os.listdir(IMAGE_FOLDER)
    if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))
])

# Keep track of current index using session state
if "page_index" not in st.session_state:
    st.session_state.page_index = 0

# Navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous"):
        if st.session_state.page_index > 0:
            st.session_state.page_index -= 1

with col3:
    if st.button("Next ➡️"):
        if st.session_state.page_index < len(image_files) - 1:
            st.session_state.page_index += 1

# Show current image (resized)
if image_files:
    image_path = image_files[st.session_state.page_index]
    img = Image.open(image_path)

    # Resize the image to 70% of original size
    new_width = int(img.width * 0.7)
    new_height = int(img.height * 0.7)
    img = img.resize((new_width, new_height))

    st.image(img, caption=f"Page {st.session_state.page_index + 1} of {len(image_files)}", use_container_width=True)
else:
    st.warning("No images found in the folder.")
