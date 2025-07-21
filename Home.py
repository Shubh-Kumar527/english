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
