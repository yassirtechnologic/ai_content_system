import os
import re

IDEAS_FOLDER = "outputs/ideas"


def safe_filename(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text)
    return text[:80]


def generate_ideas(topic):

    print("Generating content ideas for:", topic)

    os.makedirs(IDEAS_FOLDER, exist_ok=True)

    ideas = f"""
CONTENT IDEAS ABOUT: {topic}

1 Video idea:
"5 things you must know about {topic}"

2 Video idea:
"Is {topic} a good investment?"

3 Video idea:
"The future of {topic}"

4 Video idea:
"Beginner guide to {topic}"

5 Video idea:
"Top mistakes people make with {topic}"
"""

    filename = f"{safe_filename(topic)}_ideas.txt"
    filepath = os.path.join(IDEAS_FOLDER, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(ideas)

    print("Ideas saved at:", filepath)

    return filepath