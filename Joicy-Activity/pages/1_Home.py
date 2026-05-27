import streamlit as st

st.title("🏠 Home")
st.markdown("### 🎖️ Hello, I'm Mary Joicy!")

# Hero Section
st.markdown("#### Computer Science Student | ROTC Officer | Music Lover")
st.write("""
I am a dedicated Computer Science student with a passion for technology and leadership.
As an ROTC Officer, I balance my commitment to serve the country with my love for coding.
I believe in combining creativity with logic—innovating while staying disciplined.
""")

st.markdown("---")

# Mission Statement
st.markdown("#### 🎯 My Mission")
st.info("""
To use technology and leadership to make a positive impact in the world,
all while staying true to my creative and artistic side.
""")

# Current Status
st.markdown("#### 📍 Current Journey")

c1, c2 = st.columns(2)

with c1:
    st.metric("📚 Studying", "Computer Science")

with c2:
    st.metric("🎖️ Serving", "ROTC Officer")

st.markdown("---")

# Quote
st.success("""
*"Logic + Creativity = Innovation"*  
— Mary Joicy
""")