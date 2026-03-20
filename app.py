import streamlit as st

st.set_page_config(page_title="Pitpouti Clips Publisher", page_icon="🎬")

if "clips_generated" not in st.session_state:
    st.session_state.clips_generated = False

if "tiktok_connected" not in st.session_state:
    st.session_state.tiktok_connected = False

st.title("Pitpouti — AI Video Clips to TikTok")
st.write("Turn long videos into short vertical clips and upload them to TikTok.")

youtube_url = st.text_input(
    "YouTube URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

st.subheader("1. Generate clips")

if st.button("Generate Clips"):
    if youtube_url:
        st.session_state.clips_generated = True
        st.success("3 clips generated successfully.")
    else:
        st.warning("Please enter a YouTube URL.")

if st.session_state.clips_generated:
    st.write("### Generated clips")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.caption("Clip 1 — 00:00 to 00:15")

    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.caption("Clip 2 — 00:16 to 00:30")

    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.caption("Clip 3 — 00:31 to 00:45")

st.subheader("2. Connect TikTok")

if st.button("Connect TikTok"):
    st.session_state.tiktok_connected = True
    st.success("TikTok account connected successfully.")

st.subheader("3. Upload selected clip")

selected_clip = st.selectbox(
    "Choose a clip to upload",
    ["Clip 1", "Clip 2", "Clip 3"],
    index=0
)

if st.button("Upload to TikTok"):
    if not st.session_state.clips_generated:
        st.warning("Please generate clips first.")
    elif not st.session_state.tiktok_connected:
        st.warning("Please connect your TikTok account first.")
    else:
        st.success(f"{selected_clip} uploaded to TikTok successfully.")

st.markdown("---")
st.markdown("[Privacy Policy](https://mouhounamine.github.io/TON-REPO/privacy.html)")
st.markdown("[Terms of Service](https://mouhounamine.github.io/TON-REPO/terms.html)")