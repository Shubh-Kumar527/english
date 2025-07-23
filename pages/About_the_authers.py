

import streamlit as st
from PIL import Image
import os

# Use default page config for consistency with other pages
st.set_page_config(
    page_title="Meet the Authors",
    page_icon="📝",
    layout="wide"
)

st.markdown(
    "<div style='text-align: center; padding: 1rem; background-color: #f9f9f9; border-radius: 10px;'>"
    "<h1 style='color: #333;'>📝 Meet the Authors</h1>"
    "<p style='color: #666;'>Get to know the brilliant minds behind the words.</p>"
    "</div>",
    unsafe_allow_html=True
)

# Author data: name, filename, and bio
authors = [
    {"name": "J.K. Rowling", "file": "jk_rowling.jpg", "bio": "..."},
    {"name": "William Shakespeare", "file": "william_shakespeare.jpg", "bio": "..."},
    {"name": "Ruskin Bond", "file": "ruskin_bond.jpg", "bio": "..."},
    {"name": "Charles Dickens", "file": "charles_dickens.jpg", "bio": "..."},
    {"name": "Roald Dahl", "file": "roald_dahl.jpg", "bio": "..."},
    {"name": "Mark Twain", "file": "mark_twain.jpg", "bio": "..."},
    {"name": "Jane Austen", "file": "jane_austen.jpg", "bio": "..."},
    {"name": "George Orwell", "file": "george_orwell.jpg", "bio": "..."},
    {"name": "Virginia Woolf", "file": "virginia_woolf.jpg", "bio": "..."},
    {"name": "Sudha Murty", "file": "sudha_murty.jpg", "bio": "..."}
]

image_folder = "images"

if "selected_author" not in st.session_state:
    st.session_state.selected_author = None

st.markdown("<br>", unsafe_allow_html=True)

# Show authors in rows of 3
for i in range(0, len(authors), 3):
    row = authors[i:i+3]
    cols = st.columns(len(row))
    for j, author in enumerate(row):
        with cols[j]:
            try:
                img_path = os.path.join(image_folder, author["file"])
                img = Image.open(img_path)
                st.image(img, width=200, caption=author["name"])
            except FileNotFoundError:
                st.warning(f"Image for {author['name']} not found.")
            if st.button(f"Find out more about {author['name']}", key=author["name"]):
                st.session_state.selected_author = author

# Show selected author bio
if st.session_state.selected_author:
    st.markdown("---")
    st.markdown(
        f"<div style='background-color: #f0f2f6; padding: 1rem; border-radius: 10px;'>"
        f"<h3>📖 About {st.session_state.selected_author['name']}</h3>"
        f"<p style='color: #444;'>{st.session_state.selected_author['bio']}</p>"
        f"</div>",
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #999;'>"
    "&copy; 2025 English Exhibition. All rights reserved."
    "</div>",
    unsafe_allow_html=True
)
