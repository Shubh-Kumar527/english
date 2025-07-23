import streamlit as st

# Hide the default Streamlit button styling for our form
st.markdown("""
    <style>
    .custom-button {
        background-color: #4CAF50;      /* Green background */
        border: none;
        color: white;                   /* Text color */
        padding: 12px 30px;             /* Size inside button */
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 10px 0px;
        border-radius: 10px;            /* Rounded corners */
        transition-duration: 0.3s;
        cursor: pointer;
    }

    .custom-button:hover {
        background-color: white;        /* On hover */
        color: black;
        border: 2px solid #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Set up form to catch button click
with st.form(key="styled_button_form"):
    st.markdown('<button class="custom-button" type="submit">Go to Page</button>', unsafe_allow_html=True)
    submitted = st.form_submit_button()

if submitted:
    st.success("Button clicked!")  # Replace this with your action, e.g., st.switch_page("pages/Page1.py")





import streamlit as st

st.set_page_config(page_title="English Exhibition", initial_sidebar_state="collapsed")

st.title("🏫 English Exhibition")
st.markdown("### Welcome to our project!")
st.markdown("---")
st.write("Explore the world of English through our exhibition.")

# Navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📝 Go to Page One"):
        st.switch_page("pages/About_the_authers.py")
    if st.button("🎨 Go to Page Two"):
        st.switch_page("pages/page2.py")

# ----------------------------------------

import streamlit as st
from PIL import Image
import os

def about_the_auther(name):
    st.write(name)

st.title("📝 Meet the Authors")

# Author data: name, filename, and bio
authors = [
    {
        "name": "J.K. Rowling",
        "file": "jk_rowling.jpg",
        "bio": "J.K. Rowling is a British author best known for the Harry Potter series, which became a global phenomenon and one of the best-selling book series of all time. Her imaginative world of magic, Hogwarts, and characters like Harry, Hermione, and Ron captivated readers worldwide. Besides fantasy fiction, she writes crime novels under the pseudonym Robert Galbraith. Rowling’s journey from struggling single mother to literary superstar is inspiring. She is also a philanthropist, supporting children’s welfare through the Lumos charity. Her work has influenced an entire generation and transformed young adult literature."
    },
    {
        "name": "William Shakespeare",
        "file": "william_shakespeare.jpg",
        "bio": "William Shakespeare, born in 1564, is considered the greatest playwright in the English language. He wrote 39 plays, 154 sonnets, and numerous poems. His works—Hamlet, Macbeth, Romeo and Juliet, Othello—explore themes like love, power, betrayal, and human nature. Shakespeare’s influence extends beyond literature into theater, language, and popular culture. His innovative use of iambic pentameter and dramatic structure set the foundation for modern drama. His works have been translated into every major language and performed more than those of any other playwright. Despite living over 400 years ago, his words remain timeless and universally relevant."
    },
    {
        "name": "Ruskin Bond",
        "file": "ruskin_bond.jpg",
        "bio": "Ruskin Bond is a beloved Indian author who writes in English. Born in 1934, his stories often reflect life in the hills of India, especially Mussoorie. His first novel, The Room on the Roof, won the John Llewellyn Rhys Prize. Bond’s simple, heartfelt narratives explore childhood, nature, and human relationships. His books—Rusty the Boy from the Hills, Time Stops at Shamli, and others—have become staples in Indian literature for children and young adults. He writes with warmth and sensitivity, capturing the magic of everyday life. Ruskin Bond has received many awards, including the Padma Shri and Padma Bhushan."
    },
    {
        "name": "Charles Dickens",
        "file": "charles_dickens.jpg",
        "bio": "Charles Dickens (1812–1870) was one of the most famous Victorian novelists. His stories, such as Oliver Twist, David Copperfield, Great Expectations, and A Christmas Carol, focused on social injustice, poverty, and the plight of the underprivileged. Dickens used his writing to highlight the harsh realities of industrial-era England, often drawing from his own difficult childhood. His vivid characters—like Ebenezer Scrooge and Oliver Twist—remain iconic. Dickens's serialized storytelling style kept readers eagerly waiting for each chapter. His blend of humor, drama, and moral lessons continues to impact literature and social thought even today."
    },
    {
        "name": "Roald Dahl",
        "file": "roald_dahl.jpg",
        "bio": "Roald Dahl (1916–1990) was a British author best known for his imaginative and sometimes darkly humorous children's books. His classics—Charlie and the Chocolate Factory, Matilda, The BFG, and James and the Giant Peach—feature clever children, strange creatures, and unexpected twists. Dahl’s storytelling is filled with unique vocabulary, creative plots, and often a touch of the grotesque. He was also a fighter pilot and screenwriter. His books often carry subtle moral lessons and celebrate courage, kindness, and wit. With more than 250 million copies sold worldwide, Dahl remains one of the most popular children’s authors of all time."
    },
    {
        "name": "Mark Twain",
        "file": "mark_twain.jpg",
        "bio": "Mark Twain, the pen name of Samuel Langhorne Clemens (1835–1910), was an American author and humorist. He is most famous for The Adventures of Tom Sawyer and Adventures of Huckleberry Finn, which portray life along the Mississippi River. Twain's works explore themes of childhood, racism, freedom, and human nature with wit and satire. Known for his sharp observations and storytelling flair, he was also a lecturer and traveler. Twain’s writing combines humor with serious social commentary, making him a pioneer of American literature. His style influenced many authors and remains widely studied and appreciated today."
    },
    {
        "name": "Jane Austen",
        "file": "jane_austen.jpg",
        "bio": "Jane Austen (1775–1817) was an English novelist known for her keen insights into 19th-century British society. Her six major novels—Pride and Prejudice, Sense and Sensibility, Emma, and Persuasion—focus on themes of love, class, family, and marriage. Austen’s writing is known for its wit, irony, and strong, independent female characters. She highlighted the limited roles available to women and the importance of marrying well in her time. Though her work received modest success during her life, Austen is now considered one of the greatest English novelists. Her novels remain widely read and adapted for film and television."
    },
    {
        "name": "George Orwell",
        "file": "george_orwell.jpg",
        "bio": "George Orwell (1903–1950), born Eric Arthur Blair, was an English novelist, journalist, and critic. He is best known for his dystopian novels Animal Farm and Nineteen Eighty-Four, which explore themes of power, control, and totalitarianism. Orwell was a strong advocate for truth and freedom, drawing on his experiences in war and politics. His writing is clear, direct, and deeply critical of oppressive systems. Terms like “Big Brother” and “Orwellian” come from his works and are widely used today. Orwell’s sharp political insights and concern for justice make his work especially relevant in the modern world."
    },
    {
        "name": "Virginia Woolf",
        "file": "virginia_woolf.jpg",
        "bio": "Virginia Woolf (1882–1941) was a British modernist writer and a key figure in feminist literature. Known for novels like Mrs Dalloway, To the Lighthouse, and Orlando, she pioneered stream-of-consciousness writing, capturing the inner thoughts of her characters. Woolf’s essays, especially A Room of One’s Own, argued for women’s intellectual freedom and the need for financial independence. She was a central figure in the Bloomsbury Group, a circle of influential artists and thinkers. Her innovative narrative techniques and exploration of gender, time, and identity have left a lasting legacy in literature and feminist thought."
    },
    {
        "name": "Sudha Murty",
        "file": "sudha_murty.jpg",
        "bio": "Sudha Murty is an Indian author, social worker, and chairperson of the Infosys Foundation. Writing in both English and Kannada, her stories reflect values like honesty, simplicity, and kindness. Her popular books—Wise and Otherwise, Dollar Bahu, and The Old Man and His God—draw from real-life experiences and Indian culture. Murty’s writing is accessible and inspirational, appealing to readers of all ages. She is also known for her philanthropic work in education, healthcare, and rural development. In 2024, she was nominated to the Rajya Sabha. Sudha Murty’s life and work continue to influence and uplift millions."
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
st.image(image, caption="Can you recognize this famous author?", use_container_width=True)

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
        st.rerun()
