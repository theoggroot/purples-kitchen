import streamlit as st
from utils import add_custom_css, show_glass_header_title, show_glass_card
from data import get_all_ingredients_flat

st.set_page_config(page_title="Ingredients", layout="centered")
add_custom_css()

if "selected_dish" not in st.session_state:
    st.switch_page("app.py")

dish = st.session_state["selected_dish"]
pref = st.session_state.get("preference", "Veg")

# 1. Glass Header
show_glass_header_title("The Pantry 🍅")

# 2. Glass Info Card (Fixes the text visibility issue)
show_glass_card(f"Cooking Mode: {dish}", f"Dietary Preference: {pref}", icon="🥗")

all_items = get_all_ingredients_flat()
if pref == "Veg":
    blacklist = ["Chicken", "Egg", "Mutton", "Fish", "Prawns", "Crab"]
    all_items = [x for x in all_items if not any(b in x for b in blacklist)]

# 3. Wrap the selector in a glass card too for consistency
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.write("### Select your ingredients:")
selected = st.multiselect(
    "Search 150+ Ingredients:",
    options=all_items,
    placeholder="Type 'Paneer', 'Rice', 'Onion'..."
)
st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

if st.button("🔥 Find My Recipe", type="primary"):
    if not selected:
        st.error("Please pick at least one ingredient!")
    else:
        st.session_state["ingredients"] = selected
        st.switch_page("pages/4_Results.py")