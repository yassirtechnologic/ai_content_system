import os
import re

from moviepy import (
    TextClip,
    ImageClip,
    AudioFileClip,
    CompositeVideoClip,
    concatenate_videoclips
)

from config import VIDEOS_FOLDER
from utils import safe_filename


# -----------------------------
# limpiar texto
# -----------------------------

def clean_text(text):

    text = text.replace("*", "")
    text = text.replace("#", "")
    text = text.replace("[", "")
    text = text.replace("]", "")

    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# -----------------------------
# dividir script en frases
# -----------------------------

def split_script(script):

    sentences = re.split(r'[.!?]', script)

    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]

    return sentences[:6]


# -----------------------------
# generar video viral
# -----------------------------

def generate_viral_video(topic, script, images, voice, music):

    print("Creating VIRAL video for:", topic)

    os.makedirs(VIDEOS_FOLDER, exist_ok=True)

    filename = f"{safe_filename(topic)}_viral.mp4"
    video_path = os.path.join(VIDEOS_FOLDER, filename)

    width = 1080
    height = 1920

    sentences = split_script(script)

    duration_per_scene = 3

    scenes = []

    # -----------------------------
    # validar imagenes
    # -----------------------------

    valid_images = []

    for img in images:

        if isinstance(img, str) and os.path.exists(img):

            valid_images.append(img)

        else:

            print("Skipping invalid image:", img)

    if not valid_images:

        raise Exception("No valid images found for video")

    # -----------------------------
    # crear escenas
    # -----------------------------

    for i, sentence in enumerate(sentences):

        img = valid_images[i % len(valid_images)]

        print("Using image:", img)

        background = (
            ImageClip(img)
            .resized(height=height)
            .with_duration(duration_per_scene)
        )

        text = clean_text(sentence)

        subtitle = TextClip(
            text=text,
            font_size=80,
            color="white",
            stroke_color="black",
            stroke_width=3,
            size=(900, None),
            method="caption"
        )

        subtitle = subtitle.with_position(("center", "bottom")).with_duration(duration_per_scene)

        scene = CompositeVideoClip([background, subtitle])

        scenes.append(scene)

    # -----------------------------
    # unir escenas
    # -----------------------------

    slideshow = concatenate_videoclips(scenes)

    video = slideshow

    # -----------------------------
    # voz narrada
    # -----------------------------

    if voice and os.path.exists(voice):

        print("Adding voice narration")

        narration = AudioFileClip(voice)

        video = video.with_audio(narration)

    # -----------------------------
    # música de fondo
    # -----------------------------

    if music and os.path.exists(music):

        print("Adding background music")

        music_clip = AudioFileClip(music)

        if music_clip.duration > video.duration:

            music_clip = music_clip.subclip(0, video.duration)

    # -----------------------------
    # exportar video
    # -----------------------------

    video.write_videofile(
        video_path,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        bitrate="800k"
    )

    print("Viral video saved at:", video_path)

    return video_path