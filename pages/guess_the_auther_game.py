




import streamlit as st
import random
from PIL import Image
import os

# Set up the page
st.set_page_config(
    page_title="Guess the Author",
    page_icon="👀",
    layout="wide"
)

st.markdown(
    "<div style='text-align: center; padding: 1rem; background-color: #f0f2f6; border-radius: 10px;'>"
    "<h1 style='color: #333;'>👀 Guess the Author!</h1>"
    "<p style='color: #555;'>Can you recognize this famous author by their photo?</p>"
    "</div>",
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
elif selected_path == "pages/students_creation.py":
        st.switch_page("pages/students_creation.py")
elif selected_path == "pages/About_the_authers.py":
        st.switch_page("pages/About_the_authers.py")
elif selected_path == "pages/game.py":
    st.switch_page("pages/game.py")
elif selected_path == "pages/about_us.py":
    st.switch_page("pages/about_us.py")


# Author data
authors = [
    {"name": "J.K. Rowling", "file": "jk_rowling.jpg", "bio": "J.K. Rowling is a British author best known for the Harry Potter series..."},
    {"name": "William Shakespeare", "file": "william_shakespeare.jpg", "bio": "William Shakespeare, born in 1564, is considered the greatest playwright..."},
    {"name": "Ruskin Bond", "file": "ruskin_bond.jpg", "bio": "Ruskin Bond is a beloved Indian author who writes in English..."},
    {"name": "Charles Dickens", "file": "charles_dickens.jpg", "bio": "Charles Dickens (1812–1870) was one of the most famous Victorian novelists..."},
    {"name": "Roald Dahl", "file": "roald_dahl.jpg", "bio": "Roald Dahl (1916–1990) was a British author best known for his imaginative..."},
    {"name": "Mark Twain", "file": "mark_twain.jpg", "bio": "Mark Twain, the pen name of Samuel Langhorne Clemens..."},
    {"name": "Jane Austen", "file": "jane_austen.jpg", "bio": "Jane Austen (1775–1817) was an English novelist known for her keen insights..."},
    {"name": "George Orwell", "file": "george_orwell.jpg", "bio": "George Orwell (1903–1950), born Eric Arthur Blair, was an English novelist..."},
    {"name": "Virginia Woolf", "file": "virginia_woolf.jpg", "bio": "Virginia Woolf (1882–1941) was a British modernist writer..."},
    {"name": "Sudha Murty", "file": "sudha_murty.jpg", "bio": "Sudha Murty is an Indian author, social worker, and chairperson..."}
]

# Initialize session state
if 'question_index' not in st.session_state:
    st.session_state.question_index = random.randint(0, len(authors)-1)
    st.session_state.options = []
    st.session_state.reveal = False

# Load current question
correct_author = authors[st.session_state.question_index]

# Setup options once
if not st.session_state.options:
    other_authors = random.sample([a for a in authors if a != correct_author], 3)
    st.session_state.options = other_authors + [correct_author]
    random.shuffle(st.session_state.options)

# Display author image in a styled box
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center;'>",
    unsafe_allow_html=True
)
img_path = os.path.join("images", correct_author["file"])
image = Image.open(img_path)
st.image(image, width=300, caption="Can you recognize this famous author?")
st.markdown("</div>", unsafe_allow_html=True)

# Show choices
names = [opt["name"] for opt in st.session_state.options]
st.markdown("<br>", unsafe_allow_html=True)
choice = st.radio("Choose the author's name:", names)

# Submit button
if st.button("🎯 Submit"):
    st.session_state.reveal = True
    if choice == correct_author["name"]:
        st.success("✅ Correct! Well done.")
    else:
        st.error(f"❌ Oops! The correct answer was **{correct_author['name']}**.")

# Show bio and Next button
if st.session_state.reveal:
    st.markdown("---")
    st.markdown(f"### 📚 About {correct_author['name']}")
    st.info(correct_author["bio"])

    if st.button("🔄 Next Question"):
        st.session_state.question_index = random.randint(0, len(authors)-1)
        st.session_state.options = []
        st.session_state.reveal = False
        st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #000;'>"
    "&copy; 2025 English Exhibition. All rights reserved."
    "</div>",
    unsafe_allow_html=True
)
