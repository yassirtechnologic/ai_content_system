import os
from openai import OpenAI
from utils import safe_filename
from config import MODEL_NAME, SCRIPTS_FOLDER

client = OpenAI()


def generate_script(topic):

    print("Generating script with AI...")

    os.makedirs(SCRIPTS_FOLDER, exist_ok=True)

    prompt = f"""
Write a short engaging YouTube video script about: {topic}

Structure:

Title
Hook (first 5 seconds to capture attention)
Main explanation
Conclusion with call-to-action

Keep it simple, engaging and suitable for social media.
"""

    response = client.responses.create(
        model=MODEL_NAME,
        input=prompt
    )

    script = response.output_text

    filename = f"{safe_filename(topic)}_script.txt"
    filepath = os.path.join(SCRIPTS_FOLDER, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(script)

    print("Script saved at:", filepath)

    return script