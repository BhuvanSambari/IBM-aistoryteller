# app.py
import streamlit as st
from generator import generate_story

st.title("Offline AI Story Generator")

prompt = st.text_area("Enter your story prompt", "A time traveler visits ancient Egypt")

if st.button("Generate Story"):
    with st.spinner("Generating story..."):
        story = generate_story(prompt)
        st.subheader("AI-Generated Story:")
        st.write(story)
