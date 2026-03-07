from config import VIDEOS_FOLDER
from utils import safe_filename
import os

def generate_video(topic, script, music):

    print("Creating video for:", topic)

    os.makedirs(VIDEOS_FOLDER, exist_ok=True)

    filename = f"{safe_filename(topic)}_video.mp4"
    video_path = os.path.join(VIDEOS_FOLDER, filename)

    # Simulación de creación de video
    with open(video_path, "w", encoding="utf-8") as f:
        f.write("VIDEO GENERATED\n")
        f.write("Topic:\n")
        f.write(topic + "\n\n")

        f.write("SCRIPT USED:\n")
        f.write(script + "\n\n")

        f.write("MUSIC FILE:\n")
        f.write(music)

    print("Video saved at:", video_path)

    return video_path