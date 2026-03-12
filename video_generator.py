from config import VIDEOS_FOLDER
from utils import safe_filename
import os
from moviepy.editor import ColorClip


def generate_video(topic, script, music):

    print("Creating video for:", topic)

    os.makedirs(VIDEOS_FOLDER, exist_ok=True)

    filename = f"{safe_filename(topic)}_video.mp4"
    video_path = os.path.join(VIDEOS_FOLDER, filename)

    clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=2)

    clip.write_videofile(
        video_path,
        fps=24,
        codec="libx264",
        audio=False,
        preset="medium",
        threads=4,
        ffmpeg_params=["-pix_fmt", "yuv420p"]
    )

    clip.close()

    print("Video saved at:", video_path)

    return video_path