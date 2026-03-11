from config import VIDEOS_FOLDER
from utils import safe_filename
import os


def generate_video(topic, script, music):

    print("Creating video for:", topic)

    os.makedirs(VIDEOS_FOLDER, exist_ok=True)

    filename = f"{safe_filename(topic)}_video.mp4"
    video_path = os.path.join(VIDEOS_FOLDER, filename)

    # Crear archivo de video simulado (binario)
    with open(video_path, "wb") as f:
        f.write(b"FAKE_VIDEO_CONTENT")

    print("Video saved at:", video_path)

    return video_path