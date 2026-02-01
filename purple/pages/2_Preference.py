import streamlit as st
from pathlib import Path
from utils import add_custom_css, show_glass_header_title

st.set_page_config(page_title="Preference", layout="centered")
add_custom_css()

if "selected_dish" not in st.session_state:
    st.switch_page("app.py")

current_file = Path(__file__)
root_dir = current_file.parent.parent
images_dir = root_dir / "assets" / "images"

# 1. Glass Header
show_glass_header_title("Dietary Preference 🌿🍖")

col1, col2 = st.columns(2)

# 2. Wrap content in HTML Glass Cards for background
with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True) # Start Card
    st.markdown("### Veg")
    st.image(str(images_dir / "veg.jpg"), width=200)
    if st.button("Pure Veg 🥦", key="veg"):
        st.session_state["preference"] = "Veg"
        st.switch_page("pages/3_Ingredients.py")
    st.markdown('</div>', unsafe_allow_html=True) # End Card

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True) # Start Card
    st.markdown("### Non-Veg")
    st.image(str(images_dir / "nonveg.jpg"), width=200)
    if st.button("Non-Veg 🍗", key="nonveg"):
        st.session_state["preference"] = "Non-Veg"
        st.switch_page("pages/3_Ingredients.py")
    st.markdown('</div>', unsafe_allow_html=True) # End Card