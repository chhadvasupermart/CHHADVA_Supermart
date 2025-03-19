import streamlit as st

# Page Configurations
st.set_page_config(page_title="AI & Biotech Startup", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            text-align: center;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            border-radius: 8px;
            border: 1px solid #ccc;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header with Animation (using markdown for styling)
st.markdown("<h1 style='text-align: center;'>🚀 AI & Biotech Startup</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>We specialize in AI-driven learning, biotech research, semiconductor advancements, and educational technology.</p>", unsafe_allow_html=True)

# Contact Form Section
st.markdown("### 📩 Contact Us")

# Streamlit Form for user input
with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Submit")

    # Handle Form Submission
    if submit:
        if name and email and message:
            st.success("✅ Submitted Successfully!")
            st.write(f"**Name:** {name}")
            st.write(f"**Email:** {email}")
            st.write(f"**Message:** {message}")
        else:
            st.error("⚠️ Please fill out all fields before submitting.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 AI & Biotech Startup. All rights reserved.</p>", unsafe_allow_html=True)
