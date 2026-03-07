import os
import re
from config import THUMBNAILS_FOLDER


def safe_filename(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text)
    return text[:80]


def generate_thumbnail(topic):

    print("Generating thumbnail for:", topic)

    os.makedirs(THUMBNAILS_FOLDER, exist_ok=True)

    filename = f"{safe_filename(topic)}_thumbnail.png"
    path = os.path.join(THUMBNAILS_FOLDER, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write("THUMBNAIL PLACEHOLDER")

    print("Thumbnail saved at:", path)

    return path