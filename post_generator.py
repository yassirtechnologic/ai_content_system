import os
import re
from config import POSTS_FOLDER


def safe_filename(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text)
    return text[:80]


def generate_post(topic):

    print("Generating social media post for:", topic)

    os.makedirs(POSTS_FOLDER, exist_ok=True)

    post_content = f"""
POST TITLE: {topic}

INSTAGRAM CAPTION:
Discover what's happening with {topic} today.

LINKEDIN POST:
Insights and updates about {topic}. Stay informed and ahead of the market.

YOUTUBE DESCRIPTION:
In this video we explore {topic} and what it means for investors.

HASHTAGS:
#{topic.replace(" ", "")} #investing #crypto #finance #market
"""

    filename = f"{safe_filename(topic)}_post.txt"
    filepath = os.path.join(POSTS_FOLDER, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(post_content)

    print("Post saved at:", filepath)

    return filepath