from openai import OpenAI
import os
import re
from config import MODEL_NAME, POSTS_FOLDER

client = OpenAI()


def safe_filename(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text)
    return text[:80]


def generate_social_post(topic):

    print("Generating social media post for:", topic)

    os.makedirs(POSTS_FOLDER, exist_ok=True)

    prompt = f"""
Create a professional LinkedIn and Instagram post about: {topic}

Requirements:
- Strong hook in the first line
- 2–3 short paragraphs
- Practical value for entrepreneurs
- Friendly and motivational tone
- End with a call-to-action
- Include 5 relevant hashtags
"""

    response = client.responses.create(
        model=MODEL_NAME,
        input=prompt
    )

    post = response.output_text

    filename = f"{safe_filename(topic)}_post.txt"
    filepath = os.path.join(POSTS_FOLDER, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(post)

    print("Post saved at:", filepath)

    return post