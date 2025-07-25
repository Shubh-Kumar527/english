# Navigation bar
# # Navigation menu dictionary
menu = {
    "Home": "Home.py",
    "About Authors": "pages/About_the_authers.py",
    "Students Creation": "pages/students_creation.py",
    "Game": "pages/game.py",
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
elif selected_path == "pages/About_the_authers.py":
        st.switch_page("pages/About_the_authers.py")
elif selected_path == "pages/students_creation.py":
    st.switch_page("pages/students_creation.py")
elif selected_path == "pages/game.py":
    st.switch_page("pages/game.py")
elif selected_path == "pages/about_us.py":
    st.switch_page("pages/about_us.py")


