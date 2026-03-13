from openai_client import generate_ai_text
from utils import safe_filename
from config import SCRIPTS_FOLDER

import os


def generate_script(topic):

    print("Generating script with AI...")

    prompt = f"""
Create a short engaging script for a social media video about:

{topic}

The script should include:

Hook (first 5 seconds)
Main content
Call to action

Keep it short and engaging.
"""

    script = generate_ai_text(prompt)

    os.makedirs(SCRIPTS_FOLDER, exist_ok=True)

    filename = f"{safe_filename(topic)}_script.txt"
    path = os.path.join(SCRIPTS_FOLDER, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(script)

    print("Script saved at:", path)

    return script