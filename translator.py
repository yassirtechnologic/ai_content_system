from openai import OpenAI
from dotenv import load_dotenv
from config import MODEL_NAME
import os

load_dotenv()

client = OpenAI()


def translate_text(text, target_language):

    try:

        prompt = f"""
Translate the following text into {target_language}.

Return ONLY the translated text.
Do not add explanations.

Text:
{text}
"""

        response = client.responses.create(
            model=MODEL_NAME,
            input=prompt
        )

        translated_text = response.output_text.strip()

        return translated_text

    except Exception as e:

        print("Translation error:", e)
        return text