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
