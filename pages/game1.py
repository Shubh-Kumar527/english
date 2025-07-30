import streamlit as st

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
        <h1 style='color: #2c3e50;'>🎨 Game 1</h1>
        <p style='color: #34495e;'>Literary Exploration.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Navigation bar
# # Navigation menu dictionary
menu = {
    "Home": "Home.py",
    "About Authors": "pages/About_the_authers.py",
    "Students Creation": "pages/students_creation.py",
    "Brain Battles": "pages/game.py",
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


st.set_page_config(page_title="Literary Quiz", layout="wide")

# -------------------------------
# Question Data
# -------------------------------
questions = [
    {
        "question": '"Be the change that you wish to see in the world."',
        "options": ["Nelson Mandela", "Mahatma Gandhi", "Martin Luther King Jr.", "Dalai Lama"],
        "answer": "Mahatma Gandhi"
    },
    {
        "question": '"If you judge people, you have no time to love them."',
        "options": ["Mother Teresa", "Eleanor Roosevelt", "Oprah Winfrey", "Anne Frank"],
        "answer": "Mother Teresa"
    },
    {
        "question": '"Success is not final, failure is not fatal: It is the courage to continue that counts."',
        "options": ["Winston Churchill", "Theodore Roosevelt", "Abraham Lincoln", "Steve Jobs"],
        "answer": "Winston Churchill"
    },
    {
        "question": '"Imagination is more important than knowledge."',
        "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
        "answer": "Albert Einstein"
    },
    {
        "question": '"Not all those who wander are lost."',
        "options": ["C.S. Lewis", "George R.R. Martin", "J.R.R. Tolkien", "William Wordsworth"],
        "answer": "J.R.R. Tolkien"
    },
    {
        "question": '"After all this time?" "Always," said Snape.',
        "options": ["Harry Potter and the Goblet of Fire", "Harry Potter and the Half-Blood Prince", 
                    "Harry Potter and the Order of the Phoenix", "Harry Potter and the Deathly Hallows"],
        "answer": "Harry Potter and the Deathly Hallows"
    },
    {
        "question": '"My only love sprung from my only hate!"',
        "options": ["Macbeth", "Hamlet", "Romeo and Juliet", "Othello"],
        "answer": "Romeo and Juliet"
    },
    {
        "question": '"Just because someone hurts you doesn’t mean you can simply stop loving them."',
        "options": ["Verity by Colleen Hoover", "Reminders of Him by Colleen Hoover", 
                    "It Ends With Us by Colleen Hoover", "Ugly Love by Colleen Hoover"],
        "answer": "It Ends With Us by Colleen Hoover"
    },
    {
        "question": '"I could easily forgive his pride if he had not mortified mine."',
        "options": ["Emma", "Sense and Sensibility", "Mansfield Park", "Pride and Prejudice"],
        "answer": "Pride and Prejudice"
    },
    {
        "question": '"The poor and the middle class work for money. The rich have money work for them."',
        "options": ["The Intelligent Investor", "Think and Grow Rich", "Rich Dad Poor Dad", "The Psychology of Money"],
        "answer": "Rich Dad Poor Dad"
    },
]

total_questions = len(questions)

# -------------------------------
# Session State Setup
# -------------------------------
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers = [None] * total_questions
if "submitted_flags" not in st.session_state:
    st.session_state.submitted_flags = [False] * total_questions
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False


# -------------------------------
# Navigation Functions
# -------------------------------
def next_question():
    if st.session_state.current_question < total_questions - 1:
        st.session_state.current_question += 1

def prev_question():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1

def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.answers = [None] * total_questions
    st.session_state.submitted_flags = [False] * total_questions
    st.session_state.quiz_completed = False
    st.rerun()

def complete_quiz():
    st.session_state.quiz_completed = True


# -------------------------------
# Main UI
# -------------------------------
st.title("📚 Literary Exploration ")

q_index = st.session_state.current_question
q = questions[q_index]

# Progress bar and score
answered_count = sum(st.session_state.submitted_flags)
score = sum([
    1 for i, a in enumerate(st.session_state.answers)
    if st.session_state.submitted_flags[i] and a == questions[i]["answer"]
])
st.progress(answered_count / total_questions)
st.metric("Score", f"{score} / {total_questions}")

# Display current question
st.markdown(f"### Question {q_index + 1} of {total_questions}")
st.markdown(f"**{q['question']}**")

# Disable radio if already submitted
disabled = st.session_state.submitted_flags[q_index]

# Answer selection
selected = st.radio(
    "Choose an answer:",
    q["options"],
    index=q["options"].index(st.session_state.answers[q_index]) if st.session_state.answers[q_index] else 0,
    key=f"radio_{q_index}",
    disabled=disabled
)

# Store current answer selection
if not disabled:
    st.session_state.answers[q_index] = selected

# Submit button
if not disabled:
    if st.button("✅ Submit Answer"):
        st.session_state.submitted_flags[q_index] = True
        if q_index == total_questions - 1:
            complete_quiz()
        st.rerun()
else:
    # Feedback
    if st.session_state.answers[q_index] == q["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. Correct answer: {q['answer']}")

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    st.button("⬅️ Previous", on_click=prev_question, disabled=(q_index == 0))
with col2:
    st.button("➡️ Next", on_click=next_question, disabled=(q_index == total_questions - 1 or not st.session_state.submitted_flags[q_index]))

# Final summary
if st.session_state.quiz_completed:
    st.divider()
    st.success(f"🎉 Quiz Complete! Final Score: {score} / {total_questions}")
    with st.expander("View Answers"):
        for i, q in enumerate(questions):
            user = st.session_state.answers[i]
            correct = q["answer"]
            if user == correct:
                st.markdown(f"✅ **Q{i+1} Correct** — {q['question']}")
            else:
                st.markdown(f"❌ **Q{i+1} Incorrect** — Your answer: _{user}_ | Correct: _{correct}_")

# Reset
st.divider()
st.button("🔄 Reset Quiz", on_click=reset_quiz)
