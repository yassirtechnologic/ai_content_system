import os
import re
from config import MUSIC_FOLDER


def safe_filename(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text)
    return text[:80]


def generate_music(topic):

    print("Generating background music for:", topic)

    os.makedirs(MUSIC_FOLDER, exist_ok=True)

    filename = f"{safe_filename(topic)}_music.mp3"
    music_file = os.path.join(MUSIC_FOLDER, filename)

    # Placeholder for generated music
    with open(music_file, "wb") as f:
        f.write(b"")

    print("Music saved at:", music_file)

    return music_file