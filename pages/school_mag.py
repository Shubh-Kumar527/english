import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io
import os

# ---------- CONFIG ----------
st.set_page_config(layout="wide")
st.markdown(
    "<div style='text-align: center; padding: 1rem; background-color: #f9f9f9; border-radius: 10px;'>"
    "<h1 style='color: #333;'>📝 Meet the Authors</h1>"
    "<p style='color: #666;'>Get to know the brilliant minds behind the words.</p>"
    "</div>",
    unsafe_allow_html=True
)

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

st.markdown("<br>", unsafe_allow_html=True)

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



st.markdown("<br>", unsafe_allow_html=True)

# 📌 Change this to set the width of the image (in pixels)
display_width = 700

# 🔧 Set the full path to your local PDF file
pdf_path = "1.pdf"  # <- CHANGE THIS

# ---------- LOAD AND DISPLAY ----------
if not os.path.exists(pdf_path):
    st.error(f"File not found at:\n`{pdf_path}`")
else:
    doc = fitz.open(pdf_path)

    # Initialize page number if not already set
    if "page_number" not in st.session_state:
        st.session_state.page_number = 0

    # Load and render the current page
    page = doc[st.session_state.page_number]
    zoom = 2  # You can also make this a variable if you want to control zoom level
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
    img = Image.open(io.BytesIO(pix.tobytes("png")))

    # Display the image with controlled width
    st.image(img, width=display_width)

    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅️ Back") and st.session_state.page_number > 0:
            st.session_state.page_number -= 1
    with col3:
        if st.button("Next ➡️") and st.session_state.page_number < len(doc) - 1:
            st.session_state.page_number += 1

    # Page info
    st.markdown(f"**Page {st.session_state.page_number + 1} of {len(doc)}**")
