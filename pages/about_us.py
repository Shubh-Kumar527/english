import streamlit as st
import os
from PIL import Image
import base64

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
        <h1 style='color: #2c3e50;'>🎨 know about the developers</h1>
        <p style='color: #34495e;'>Explore original work made by our talented students.</p>
    </div>
    """,
    unsafe_allow_html=True
)
