import streamlit as st
import random
from PIL import Image

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

# Display author image
st.title("👀 Guess the Author!")
image = Image.open(f"images/{correct_author['file']}")
st.image(image, caption="Can you recognize this famous author?", use_column_width=True)

# Show choices
names = [opt["name"] for opt in st.session_state.options]
choice = st.radio("Choose the author's name:", names)

# Submit button
if st.button("Submit"):
    st.session_state.reveal = True
    if choice == correct_author["name"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Wrong! The correct answer was **{correct_author['name']}**.")

# Show bio and Next button
if st.session_state.reveal:
    st.markdown("### 📚 About the Author")
    st.info(correct_author["bio"])
    
    if st.button("Next"):
        st.session_state.question_index = random.randint(0, len(authors)-1)
        st.session_state.options = []
        st.session_state.reveal = False
        st.experimental_rerun()
