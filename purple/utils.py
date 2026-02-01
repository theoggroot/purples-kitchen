import streamlit as st
import base64
from pathlib import Path

# --- ERROR FIX: No "from utils import..." here! ---

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

def add_custom_css():
    # 1. SETUP PATHS
    current_dir = Path(__file__).parent
    bg_image_path = current_dir / "assets" / "images" / "bg.jpg"
    
    # 2. GENERATE BACKGROUND
    base_bg_css = ".stApp { background-color: #f0f2f6; }"
    
    if bg_image_path.exists():
        bin_str = get_base64_of_bin_file(bg_image_path)
        if bin_str:
            base_bg_css = f"""
                .stApp {{ background: transparent; }}
                .stApp::before {{
                    content: "";
                    position: fixed;
                    top: 0; left: 0; width: 100vw; height: 100vh;
                    background-image: url("data:image/jpg;base64,{bin_str}");
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    filter: blur(5px);
                    transform: scale(1.02);
                    z-index: -1; 
                }}
            """

    # 3. INJECT CSS (The Whitish Glass Look)
    st.markdown(f"""
        <style>
        {base_bg_css}
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Poppins', sans-serif;
            color: #000000 !important;
        }}

        /* --- GLASS HEADER (Titles) --- */
        .glass-header {{
            background-color: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            border: 2px solid rgba(255, 255, 255, 1);
            border-radius: 20px;
            padding: 15px;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }}
        .glass-header h1 {{
            color: #6C5CE7 !important;
            margin: 0;
            text-shadow: 2px 2px 0px rgba(255,255,255,0.8);
        }}

        /* --- GLASS CARD (Content) --- */
        .glass-card {{
            background-color: rgba(255, 255, 255, 0.90) !important; /* 90% White */
            backdrop-filter: blur(15px);
            border: 2px solid white;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            border-radius: 20px;
            padding: 25px;
            margin-bottom: 20px;
        }}
        
        /* TEXT COLORS */
        h1, h2, h3, h4, .glass-card h3 {{ color: #1a1a1a !important; font-weight: 700; margin-top: 0; }}
        p, li, .stMarkdown, .stText {{ color: #000000 !important; font-weight: 500; }}

        /* --- FIX DROPDOWNS & INPUTS --- */
        .streamlit-expanderHeader {{
            background-color: rgba(255, 255, 255, 0.95) !important;
            color: #000000 !important;
            border-radius: 10px;
            border: 1px solid #ddd;
        }}
        div[data-testid="stExpanderDetails"] {{
            background-color: rgba(255, 255, 255, 0.90) !important;
            border-radius: 0 0 10px 10px;
            color: #000000 !important;
        }}
        
        /* IMAGES */
        img {{ border-radius: 15px; border: 3px solid white; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }}

        /* BUTTONS */
        div.stButton > button {{
            background: linear-gradient(90deg, #a29bfe, #6c5ce7);
            color: white !important;
            border: none; padding: 10px 20px; border-radius: 12px;
            font-weight: 600; width: 100%; transition: 0.3s;
        }}
        div.stButton > button:hover {{ transform: translateY(-2px); }}
        </style>
    """, unsafe_allow_html=True)

def show_glass_header_title(title):
    st.markdown(f'<div class="glass-header"><h1>{title}</h1></div>', unsafe_allow_html=True)

def show_glass_card(title, content, icon="✨"):
    st.markdown(f"""
    <div class="glass-card">
        <h3 style="display:flex; align-items:center; gap:10px;"><span>{icon}</span> {title}</h3>
        <p>{content}</p>
    </div>""", unsafe_allow_html=True)