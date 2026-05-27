import streamlit as st

st.title("🧑‍🎓 About Me")
st.markdown("---")

# Who Am I
st.markdown("### 🎖️ Who Am I?")
st.write("""
As a Computer Science student and ROTC Officer, I balance my passion for technology 
with my commitment to serve the country. I have a strong interest in the arts 
and enjoy combining creativity with logic. Music keeps me focused while I learn coding, 
and strategy games sharpen how I think.
""")

st.markdown("---")

# Two Column Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🎯 Core Traits")
    st.markdown("""
- **Quiet but Observant**
- **Easy to Work With**
- **Quick to Adapt**
- **Disciplined**
- **Leader**
- **Detailed-oriented**
    """)

with col2:
    st.markdown("#### 💜 What Drives Me")
    st.markdown("""
- Technology & Innovation
- Leadership & Service
- Arts & Creativity
- Music & Inspiration
- Problem Solving
    """)

st.markdown("---")

# Philosophy
st.markdown("### 🌟 My Philosophy")
st.info("""
I believe that being a great coder requires both technical skills and creativity.
Likewise, being a good leader requires understanding, empathy, and the ability
to adapt to any situation. I am committed to growing in both areas every day.
""")