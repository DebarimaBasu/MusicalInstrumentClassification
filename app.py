import streamlit as st
import os
from visualization import visualize_audio

st.set_page_config(page_title="Instrument Activity Detection", layout="centered")

st.title("🎶 Instrument Activity Detection")
st.write("Upload an audio file to start visualization")

uploaded_file = st.file_uploader(
    "Choose an audio file",
    type=["mp3", "wav"]
)

if uploaded_file is not None:
    try:
        audio_path = "uploaded_audio.mp3"

        with open(audio_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success("Audio uploaded successfully")

        visualize_audio(audio_path)

    except Exception as e:
        st.error("Something went wrong")
        st.exception(e)
else:
    st.info("👆 Please upload an audio file")
