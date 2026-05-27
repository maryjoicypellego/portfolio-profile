import streamlit as st

st.set_page_config(
    page_title="Mary Joicy | My Portfolio",
    page_icon="🎖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap');
        
        * {
            font-family: 'Montserrat', sans-serif;
        }
        
        /* Navy Blue Background */
        .stApp {
            background: linear-gradient(180deg, #0a192f 0%, #112240 100%);
            color: white;
        }
        
        /* Light text for dark background */
        p, li, div {
            color: #e6f1ff !important;
        }
        
        /* Sidebar - Gold Accent */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
            border-right: 3px solid #ffd700;
        }
        
        [data-testid="stSidebar"] * {
            color: #ffd700 !important;
        }
        
        /* Headers - Gold Theme */
        h1, h2, h3, h4 {
            color: #ffd700 !important;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Info boxes styling */
        .stInfo, .stSuccess {
            background: rgba(255, 215, 0, 0.1) !important;
            border-left: 4px solid #ffd700 !important;
            color: #ffd700 !important;
        }
        
        /* Metric styling */
        [data-testid="stMetricValue"] {
            color: #ffd700 !important;
        }
        
        /* Button styling */
        .stButton>button {
            background: linear-gradient(90deg, #ffd700 0%, #ff8c00 100%);
            color: #0a192f !important;
            font-weight: 700;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎖️ Welcome to My Portfolio")
st.markdown("---")

st.write("""
**Computer Science Student | ROTC Officer | Music Lover**

Welcome to my digital portfolio. Explore my journey, skills, and passions.
""")

st.markdown("### 📊 At a Glance")

c1, c2, c3 = st.columns(3)
c1.metric("🎓 CS Student", "Active")
c2.metric("🎖️ ROTC Officer", "Dedicated")
c3.metric("🎵 Music Lover", "Always")

with st.sidebar:
    st.markdown("### 🎖️ Mary Joicy F. Pellego")
    st.caption("CS Student | Officer | Creator")
    st.markdown("---")
    st.markdown("**📍 Quick Links**")
    st.write("- Home")
    st.write("- About Me")
    st.write("- Skills")
    st.write("- Interests")
    st.write("- Contact")
    st.markdown("---")
    st.caption("© 2026 Mary Joicy Portfolio")