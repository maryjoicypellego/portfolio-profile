import streamlit as st

st.title("⚡ Skills")
st.markdown("### What I Bring to the Table")
st.write("---")

# Technical Skills
st.markdown("#### 💻 Technical Skills")

st.markdown("**Programming Fundamentals**")
st.progress(75)

st.markdown("**Digital Exploration**")
st.progress(70)

st.markdown("**Problem Solving**")
st.progress(80)

st.markdown("---")

# Leadership Skills
st.markdown("#### 🎖️ Leadership Skills")

st.markdown("**Leadership & Discipline**")
st.progress(90)

st.markdown("**Team Management**")
st.progress(85)

st.markdown("**Strategic Thinking**")
st.progress(80)

st.markdown("---")

# Creative Skills
st.markdown("#### 🎨 Creative Skills")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("💡 Creativity", "High", "")

with c2:
    st.metric("🎵 Arts", "High", "")

with c3:
    st.metric("🧩 Logic", "High", "")

st.markdown("---")

# Skill Summary
st.success("""
✅ Well-rounded: Technical + Leadership + Creative  
✅ Disciplined approach to problem solving  
✅ Always eager to learn and grow
""")