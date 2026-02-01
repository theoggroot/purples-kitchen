import streamlit as st
from utils import add_custom_css, show_glass_card, show_glass_header_title
from data import get_random_recipe_from_api, get_random_indian_recipe

st.set_page_config(page_title="Explore", layout="centered")
add_custom_css()

# --- MEMORY ---
if "seen_indian_ids" not in st.session_state:
    st.session_state["seen_indian_ids"] = []

show_glass_header_title("Random Dish Generator 🎲")

col1, col2 = st.columns(2)

with col1:
    if st.button("🌍 Global Spin", use_container_width=True):
        with st.spinner("Traveling the world..."):
            st.session_state["random_recipe"] = get_random_recipe_from_api()

with col2:
    if st.button("🇮🇳 Indian Special", use_container_width=True):
        with st.spinner("Finding spicy delights..."):
            seen = st.session_state["seen_indian_ids"]
            new_recipe = get_random_indian_recipe(seen)
            
            if new_recipe:
                if new_recipe['id'] in seen:
                    st.session_state["seen_indian_ids"] = [new_recipe['id']]
                else:
                    st.session_state["seen_indian_ids"].append(new_recipe['id'])
                st.session_state["random_recipe"] = new_recipe

# --- DISPLAY ---
if "random_recipe" in st.session_state and st.session_state["random_recipe"]:
    r = st.session_state["random_recipe"]
    
    # SAFE IMAGE LOADING
    img_url = r.get("image")
    if img_url and img_url != "None" and img_url != "":
        st.image(img_url, use_container_width=True)
    else:
        st.warning("No image available for this recipe.")

    show_glass_card(r['name'], f"Origin: {r['tags'][1]} | Category: {r['tags'][0]}", icon="🍲")
    
    with st.expander("📝 View Full Recipe", expanded=True):
        st.write("### 🛒 Ingredients:")
        for item in r.get('ingredients_needed', []):
            st.write(f"- {item}")
        
        st.write("### 🍳 Instructions:")
        for idx, step in enumerate(r.get('steps', []), 1):
            st.write(f"**{idx}.** {step}")

st.write("---")
if st.button("🏠 Home"): st.switch_page("app.py")