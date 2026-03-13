import os
import re
import numpy as np
from scipy.io.wavfile import write
from config import MUSIC_FOLDER


def safe_filename(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text)
    return text[:80]


def generate_music(topic):

    print("Generating background music for:", topic)

    os.makedirs(MUSIC_FOLDER, exist_ok=True)

    filename = f"{safe_filename(topic)}_music.wav"
    music_file = os.path.join(MUSIC_FOLDER, filename)

    duration = 10
    sample_rate = 44100
    frequency = 220

    t = np.linspace(0, duration, int(sample_rate * duration))

    audio = 0.3 * np.sin(2 * np.pi * frequency * t)

    write(music_file, sample_rate, audio.astype(np.float32))

    print("Music saved at:", music_file)

    return music_file