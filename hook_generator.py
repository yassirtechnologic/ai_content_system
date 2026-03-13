"""
HOOK GENERATOR
Creates viral hooks for the first seconds of the video
"""

from openai import OpenAI
from config import MODEL_NAME

client = OpenAI()


def generate_hook(topic):

    print("Generating viral hooks with AI...")

    prompt = f"""
You are a viral content strategist for TikTok, Instagram Reels and YouTube Shorts.

Create 5 extremely engaging hooks for a short video about:

{topic}

Rules:
- Maximum 12 words
- Very curiosity driven
- High emotional trigger
- Make the viewer want to keep watching
- Style used by viral creators

Return the hooks as a numbered list.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a viral content expert."},
            {"role": "user", "content": prompt}
        ]
    )

    text = response.choices[0].message.content

    hooks = []

    for line in text.split("\n"):

        line = line.strip()

        if line and line[0].isdigit():

            hook = line.split(".", 1)[1].strip()

            hooks.append(hook)

    if not hooks:

        return topic

    best_hook = hooks[0]

    print("Selected hook:", best_hook)

    return best_hook