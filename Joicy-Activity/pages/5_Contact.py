import streamlit as st

st.title("📞 Contact Me")
st.markdown("### Let's Connect!")
st.write("---")

# Contact Information
st.markdown("#### 🎖️ Get in Touch")

st.markdown("""
**📱 Phone:** 09709756028  
**📧 Email:** maryjoicypellego@gmail.com  
**📘 Facebook:** Mary Joicy Pellego
""")

st.markdown("---")

# Contact Form
st.markdown("#### ✉️ Send a Message")

with st.form("contact_form_mary"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send 📨")

    if submit:
        if name and email and message:
            st.success(f"Thank you, {name}! Message sent successfully! 🎖️")
        else:
            st.error("Please fill in all fields.")

st.markdown("---")
st.caption("© 2024 Mary Joicy Portfolio | Created with 💜")