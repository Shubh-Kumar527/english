import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io
import os

# ---------- CONFIG ----------
st.set_page_config(layout="centered")
st.title("📖 PDF Flip Book Viewer (Local File)")

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
