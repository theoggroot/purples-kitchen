import streamlit as st
from pathlib import Path
from utils import add_custom_css, show_glass_card, show_glass_header_title

st.set_page_config(page_title="Purple's Kitchen", page_icon="🍇", layout="wide")
add_custom_css()

# --- USE THE NEW GLASS HEADER ---
show_glass_header_title("Purple's Kitchen 🍇")
st.markdown("<h3 style='text-align: center; color: black;'>The Ultimate AI Culinary Assistant</h3>", unsafe_allow_html=True)
st.write("") # Spacer

col1, col2 = st.columns([1, 1])

with col1:
    st.image("assets/images/loading.gif", width=300)

with col2:
    # GLASS CARD 1
    show_glass_card("Chef Mode", "Follow the guided wizard to find the perfect recipe.", icon="👨‍🍳")
    if st.button("🚀 Start Cooking", key="start"):
        st.switch_page("pages/1_Dishes.py")
        
    st.write("") 
    
    # GLASS CARD 2
    show_glass_card("Surprise Me", "Spin the wheel for a random dish.", icon="🎲")
    if st.button("✨ Explore Random", key="explore"):
        st.switch_page("pages/Explore.py")