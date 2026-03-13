import streamlit as st
import json

st.set_page_config(
    page_title="AI Content System",
    layout="wide"
)

st.title("🚀 AI Content Dashboard")

with open("content_database/videos.json", "r") as f:
    videos = json.load(f)

st.write("Total videos generated:", len(videos))

st.divider()

for video in reversed(videos):

    st.subheader(video["topic"])

    st.video(video["video_url"])

    st.markdown(
        f"[Open in Cloudinary]({video['video_url']})"
    )

    st.divider()