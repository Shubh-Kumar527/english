

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="English Exhibition",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default menu and footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Main header
st.markdown(
    "<div style='text-align: center; padding: 1rem; background-color: #f0f2f6; border-radius: 10px;'>"
    "<h1 style='color: #333;'>🏫 English Exhibition</h1>"
    "<p style='color: #666; font-size: 1.1rem;'>Welcome to our project!</p>"
    "</div>",
    unsafe_allow_html=True
)

st.markdown("---")
st.write("Explore the world of English through our exhibition.")

# Navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📝 Go to Page One"):
        st.switch_page("pages/About_the_authers.py")
    if st.button("🎨 Go to Page Two"):
        st.switch_page("pages/page2.py")
    if st.button("🎨 Go to Page THree"):
        st.switch_page("pages/page3.py")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #999;'>"
    "&copy; 2025 English Exhibition. All rights reserved."
    "</div>",
    unsafe_allow_html=True
)

