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
elif selected_path == "pages/game.py":
    st.switch_page("pages/game.py")
elif selected_path == "pages/about_us.py":
    st.switch_page("pages/about_us.py")
elif selected_path == "pages/school_mag.py":
    st.switch_page("pages/school_mag.py")


# Path to your image folder
# --- CONFIG ---
IMAGE_FOLDER = "poems"

# --- LOAD IMAGES ---
image_files = sorted(
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith((".png","jpg","jpeg","gif"))
)

# --- SESSION STATE ---
if "idx" not in st.session_state:
    st.session_state.idx = 0

# --- NAVIGATION HANDLERS ---
def prev_img():
    if st.session_state.idx > 0:
        st.session_state.idx -= 1

def next_img():
    if st.session_state.idx < len(image_files) - 1:
        st.session_state.idx += 1

# --- LAYOUT: empty side columns + center column ---
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    if not image_files:
        st.warning("No images found in 'student_works' folder.")
    else:
        # Open & resize
        img = Image.open(os.path.join(IMAGE_FOLDER, image_files[st.session_state.idx]))
        max_width = 300
        ratio = img.height / img.width
        img = img.resize((max_width, int(max_width * ratio)))

        # Display
        st.image(img, width=500)
        st.caption(f"Page {st.session_state.idx + 1} of {len(image_files)}")

        # Navigation buttons
        prev_col, _, next_col = st.columns([1,1,1])
        with prev_col:
            if st.button("⬅️ Previous"):
                prev_img()
        with next_col:
            if st.button("Next ➡️"):
                next_img()
