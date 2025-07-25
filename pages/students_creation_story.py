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

# Path to image folder
IMAGE_FOLDER = "stories"

# Load image files
image_files = sorted([
    os.path.join(IMAGE_FOLDER, f)
    for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
])

# Track current image index
if "page_index" not in st.session_state:
    st.session_state.page_index = 0

# Handle navigation
def go_prev():
    if st.session_state.page_index > 0:
        st.session_state.page_index -= 1

def go_next():
    if st.session_state.page_index < len(image_files) - 1:
        st.session_state.page_index += 1

# Layout: horizontal row
col1, col2, col3 = st.columns([1, 3, 1], gap="large")

# Left button
with col1:
    st.markdown("###")  # For vertical alignment
    if st.button("⬅️", use_container_width=True):
        go_prev()

# Center image
with col2:
    if image_files:
        image_path = image_files[st.session_state.page_index]
        img = Image.open(image_path)

        # Resize portrait image
        max_width = 350
        aspect_ratio = img.height / img.width
        new_height = int(max_width * aspect_ratio)
        img = img.resize((max_width, new_height))

        # Convert to base64 for HTML rendering
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()

        # Centered image and caption
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{img_base64}" width="{max_width}px"><br>
                <p style="margin-top: 8px;">Page {st.session_state.page_index + 1} of {len(image_files)}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("No images found in the folder.")

# Right button
with col3:
    st.markdown("###")
    if st.button("➡️", use_container_width=True):
        go_next()
