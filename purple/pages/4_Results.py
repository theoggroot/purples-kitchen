import streamlit as st
from utils import add_custom_css, show_glass_header_title
from data import find_recipes_smart

st.set_page_config(page_title="Results", layout="centered")
add_custom_css()

if "ingredients" not in st.session_state:
    st.switch_page("pages/3_Ingredients.py")

user_ingredients = st.session_state["ingredients"]
category = st.session_state.get("selected_dish", "Heavy Food")
pref = st.session_state.get("preference", "Veg")

show_glass_header_title("Chef's Recommendations 🍽️")

with st.spinner(f"Searching global database for {user_ingredients[0]} recipes..."):
    matches = find_recipes_smart(category, pref, user_ingredients)

if not matches:
    st.warning("😕 No exact matches found for that ingredient combo.")
    st.info("Try selecting just ONE main ingredient (like 'Chicken' or 'Potato') for better results.")
    if st.button("Go Back"): st.switch_page("pages/3_Ingredients.py")
else:
    for match in matches: 
        recipe = match["data"]
        
        # SAFE IMAGE LOADING
        if recipe.get("image"):
            st.image(recipe["image"], width=300)

        st.markdown(f"""
        <div class="glass-card">
            <h2 style="color: #6C5CE7; margin-bottom: 5px;">{recipe['name']}</h2>
            <p>
                <span style="background:#eee; padding:5px 10px; border-radius:8px;">🌍 {recipe['tags'][1]}</span>
                <span style="background:#eee; padding:5px 10px; border-radius:8px; margin-left:10px;">🍲 {recipe['tags'][0]}</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander(f"👩‍🍳 View Recipe: {recipe['name']}"):
            t1, t2 = st.tabs(["📜 Instructions", "🛒 Ingredients"])
            with t1:
                for idx, step in enumerate(recipe['steps'], 1):
                    st.write(f"**{idx}.** {step}")
            with t2:
                for item in recipe.get('ingredients_needed', []):
                    st.write(f"- {item}")

st.markdown("---")
if st.button("🔄 Start Fresh"):
    for k in list(st.session_state.keys()): del st.session_state[k]
    st.switch_page("app.py")