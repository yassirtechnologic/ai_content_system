import os
import re
from config import SHORTS_FOLDER


def safe_filename(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text)
    return text[:80]


def generate_shorts(topic):

    print("Generating shorts script for:", topic)

    os.makedirs(SHORTS_FOLDER, exist_ok=True)

    content = f"""
SHORT VIDEO SCRIPT

Topic: {topic}

HOOK:
Did you know this about {topic}?

FAST EXPLANATION:
In less than 30 seconds we explain the key idea behind {topic}.

VALUE:
This could change the way people understand the market.

CALL TO ACTION:
Follow for more finance and tech insights.
"""

    filename = f"{safe_filename(topic)}_shorts.txt"
    filepath = os.path.join(SHORTS_FOLDER, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print("Shorts script saved at:", filepath)

    return filepath