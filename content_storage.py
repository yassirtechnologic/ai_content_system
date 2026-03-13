import json
import os

DATABASE_FILE = "content_database/videos.json"


def save_video(topic, video_url):

    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as f:
            json.dump([], f)

    with open(DATABASE_FILE, "r") as f:
        data = json.load(f)

    new_video = {
        "topic": topic,
        "video_url": video_url
    }

    data.append(new_video)

    with open(DATABASE_FILE, "w") as f:
        json.dump(data, f, indent=4)