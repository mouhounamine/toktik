import streamlit as st

st.set_page_config(page_title="Pitpouti Clips Publisher", page_icon="🎬")

st.title("Pitpouti — AI Video Clips to TikTok")
st.write("Turn long videos into short vertical clips and upload them to TikTok.")

st.subheader("1. Enter a YouTube URL")
youtube_url = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Generate Clips"):
    if youtube_url:
        st.success("3 clips generated successfully.")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    else:
        st.warning("Please enter a YouTube URL.")

st.subheader("2. Connect TikTok")
st.button("Connect TikTok")

st.subheader("3. Upload selected clip")
st.button("Upload to TikTok")

with st.expander("Privacy Policy"):
    st.write("""
    Pitpouti allows users to connect their TikTok account to upload video clips.
    We only use the minimum data required for authentication and video publishing.
    We do not sell or share personal data.
    """)

with st.expander("Terms of Service"):
    st.write("""
    Pitpouti is a video clipping and publishing tool.
    Users are responsible for the content they upload and must have the rights to use it.
    Users must comply with TikTok policies and applicable laws.
    """)