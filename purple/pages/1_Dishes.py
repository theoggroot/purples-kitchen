import streamlit as st
from pathlib import Path
from utils import add_custom_css, show_glass_header_title

st.set_page_config(page_title="Select Dish", layout="wide")
add_custom_css()

current_file = Path(__file__)
root_dir = current_file.parent.parent
images_dir = root_dir / "assets" / "images"

# Use the glass header for consistency
show_glass_header_title("What are you craving? 😋")

categories = {
    "Light Food": "light_food.jpg",
    "Heavy Food": "heavy_food.jpg",
    "Chaat / Snacks": "chaat.jpg",
    "Sweets": "sweet.jpg"
}

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
cols = [col1, col2, col3, col4]

for i, (cat, img_file) in enumerate(categories.items()):
    with cols[i]:
        # Simple container for image grid
        with st.container():
            st.markdown(f"### {cat}")
            img_path = images_dir / img_file
            
            if img_path.exists():
                st.image(str(img_path), width=200) 
            
            if st.button(f"Select", key=f"btn_{i}"):
                st.session_state["selected_dish"] = cat
                if cat in ["Sweets", "Chaat / Snacks"]:
                    st.session_state["preference"] = "Veg"
                    st.switch_page("pages/3_Ingredients.py")
                else:
                    st.switch_page("pages/2_Preference.py")