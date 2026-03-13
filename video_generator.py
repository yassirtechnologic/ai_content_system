from config import VIDEOS_FOLDER
from utils import safe_filename

import os
import re

from moviepy import (
    TextClip,
    AudioFileClip,
    CompositeVideoClip,
    ImageClip,
    concatenate_videoclips
)


def clean_text(text):

    text = text.replace("*", "")
    text = text.replace("#", "")
    text = text.replace("[", "")
    text = text.replace("]", "")

    text = text.encode("ascii", "ignore").decode()

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def split_script(script):

    sentences = re.split(r'[.!?]', script)

    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]

    return sentences[:6]


def generate_video(topic, script, music, images, voice):

    print("Creating PRO viral video for:", topic)

    os.makedirs(VIDEOS_FOLDER, exist_ok=True)

    filename = f"{safe_filename(topic)}_video.mp4"
    video_path = os.path.join(VIDEOS_FOLDER, filename)

    # formato vertical para reels
    width = 1080
    height = 1920

    # dividir script en frases
    sentences = split_script(script)

    duration_per_scene = 3

    scenes = []

    for i, sentence in enumerate(sentences):

        img = images[i % len(images)]

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

    slideshow = concatenate_videoclips(scenes)

    video = slideshow

    # ---------- VOZ IA ----------

    try:

        if voice and os.path.exists(voice):

            narration = AudioFileClip(voice)

            video = video.with_audio(narration)

    except Exception as e:

        print("Voice error:", e)

    # ---------- MUSICA ----------

    try:

        if music and os.path.exists(music):

            music_clip = AudioFileClip(music)

            if music_clip.duration > video.duration:

                music_clip = music_clip.subclipped(0, video.duration)

    except Exception as e:

        print("Music error:", e)

    # ---------- EXPORT ----------

    video.write_videofile(
        video_path,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        bitrate="800k"
    )

    print("PRO video saved at:", video_path)

    return video_path