import streamlit as st

st.title("🎮 Interests & Hobbies")
st.markdown("### What I Love to Do")
st.write("---")

# Music & Entertainment
st.markdown("#### 🎵 My Vibes")

h1, h2 = st.columns(2)

with h1:
    st.markdown("##### 🎧 Listening to Music")
    st.write("Music keeps me focused while coding and studying.")

with h2:
    st.markdown("##### 🎬 Movies & Anime")
    st.write("Entertainment that inspires my creativity.")

st.markdown("---")

# Active Hobbies
st.markdown("#### ⚡ Active Interests")

h3, h4 = st.columns(2)

with h3:
    st.markdown("##### 🎮 Strategy Games")
    st.write("Sharpening my mind with tactical thinking.")

with h4:
    st.markdown("##### 💻 Digital Exploration")
    st.write("Exploring new tech, tools, and innovations.")

st.markdown("---")

# Summary Box
st.success("""
🎖️ Whether I'm coding, serving, or creating—music and strategy 
always keep me inspired. I believe in balanced growth: 
mind, body, and creativity.
""")

st.markdown("---")

# Fun Fact
st.info("""
**Fun Fact:** I can code while listening to music—it's my 
perfect productivity combo!
""")