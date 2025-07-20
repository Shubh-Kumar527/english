import streamlit as st
from PIL import Image
import os

def about_the_auther(name):
    st.write(name)

st.title("📝 Meet the Authors")

# Author data: name, filename, and bio
authors = [
    {
        "name": "William Shakespeare",
        "file": "img4.jpg",
        "bio": "William Shakespeare was an English playwright, poet, and actor, widely regarded as the greatest writer in the English language."
    },
    {
        "name": "Jane Austen",
        "file": "img3.jpg",
        "bio": "Jane Austen was an English novelist known for her six major novels that interpret and critique British landed gentry at the end of the 18th century."
    },
    {
        "name": "Mark Twain",
        "file": "img2.jpg",
        "bio": "Mark Twain was an American writer, humorist, entrepreneur, and lecturer, best known for 'The Adventures of Tom Sawyer' and 'Adventures of Huckleberry Finn'."
    },
    {
        "name": "Charles Dickens",
        "file": "img1.jpg",
        "bio": "Charles Dickens was an English writer and social critic, famous for novels such as 'Oliver Twist', 'A Christmas Carol', and 'Great Expectations'."
    }
]

# Image folder path
image_folder = "images"

# Author clicked (used to show bio later)
if "selected_author" not in st.session_state:
    st.session_state.selected_author = None

# Show authors in rows of 3
for i in range(0, len(authors), 3):
    row = authors[i:i+3]
    cols = st.columns(len(row))
    for j, author in enumerate(row):
        with cols[j]:
            try:
                img = Image.open(os.path.join(image_folder, author["file"]))
                st.image(img, width=200, caption=author["name"])
            except FileNotFoundError:
                st.error(f"Image '{author['file']}' not found.")
            if st.button(f"Find out more about {author['name']}", key=author["name"]):
                st.session_state.selected_author = author

# Show bio at bottom
if st.session_state.selected_author:
    st.markdown("---")
    st.markdown(f"### 📖 About {st.session_state.selected_author['name']}")
    st.write(st.session_state.selected_author["bio"])

# Back button
# st.markdown("---")
# if st.button("🔙 Back to Home"):
#     st.switch_page("main.py")