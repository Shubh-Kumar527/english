import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io
import os



# 🔧 Set the full path to your local PDF here
pdf_path = "1.pdf"

# Check if file exists
if not os.path.exists(pdf_path):
    st.error(f"File not found at:\n`{pdf_path}`")
else:
    # Open the PDF
    doc = fitz.open(pdf_path)

    # Setup session state for page tracking
    if "page_number" not in st.session_state:
        st.session_state.page_number = 0

    # Display current page
    page = doc[st.session_state.page_number]
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for clarity
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    st.image(img, use_column_width=True)

    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅️ Back") and st.session_state.page_number > 0:
            st.session_state.page_number -= 1
    with col3:
        if st.button("Next ➡️") and st.session_state.page_number < len(doc) - 1:
            st.session_state.page_number += 1

    # Page number display
    st.markdown(f"**Page {st.session_state.page_number + 1} of {len(doc)}**")
