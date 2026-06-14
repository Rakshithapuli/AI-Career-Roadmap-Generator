import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AI-Career-Roadmap-Generator")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🚀 AI Career Roadmap Generator")

skills = st.text_area("Enter Your Current Skills")

target_role = st.text_input("Enter Your Target Role")

if st.button("Generate Roadmap"):

    prompt = f"""
    You are an experienced Career Mentor.

    Current Skills:
    {skills}

    Target Role:
    {target_role}

    Create:
    1. 3 Month Learning Roadmap
    2. Skills to Learn
    3. Projects to Build
    4. Interview Preparation Tips
    """

    response = model.generate_content(prompt)

    st.write(response.text)