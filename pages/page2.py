import streamlit as st
import random
from PIL import Image
import os
import json

# Hide the sidebar completely
st.set_page_config(initial_sidebar_state="collapsed")

st.title("🎯 Guess the Author")
st.markdown("Look at the picture and guess who the author is!")

# Load authors from dataset
with open("authors.json", "r", encoding="utf-8") as f:
    authors = json.load(f)

# Initialize session state
if "question_index" not in st.session_state:
    st.session_state.question_index = random.randint(0, len(authors) - 1)
    st.session_state.reveal = False
    st.session_state.options = []

# Get correct author
correct_author = authors[st.session_state.question_index]

# Display image
image_path = os.path.join("images", correct_author["file"])
image = Image.open(image_path)
st.image(image, caption="Can you recognize this famous author?", use_container_width=True)

# Generate options only once
if not st.session_state.options:
    all_other_names = [a["name"] for a in authors if a["name"] != correct_author["name"]]
    options = random.sample(all_other_names, 3) + [correct_author["name"]]
    random.shuffle(options)
    st.session_state.options = options

# Show radio button for answer
selected = st.radio("Select the author's name:", st.session_state.options)

# Show result
if st.button("Submit"):
    if selected == correct_author["name"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect! The correct answer is {correct_author['name']}")
    st.session_state.reveal = True

# Next question
if st.session_state.reveal and st.button("Next Question"):
    st.session_state.question_index = random.randint(0, len(authors) - 1)
    st.session_state.options = []
    st.session_state.reveal = False
    st.experimental_rerun()
