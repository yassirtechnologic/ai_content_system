import os
from openai import OpenAI
from config import VOICE_FOLDER
from utils import safe_filename

client = OpenAI()


def generate_voice(topic, script):

    print("Generating voice with OpenAI TTS...")

    os.makedirs(VOICE_FOLDER, exist_ok=True)

    filename = f"{safe_filename(topic)}_voice.mp3"
    voice_path = os.path.join(VOICE_FOLDER, filename)

    try:

        response = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=script[:1500]  # limitamos texto para evitar audios muy largos
        )

        with open(voice_path, "wb") as f:
            f.write(response.content)

        print("Voice saved at:", voice_path)

        return voice_path

    except Exception as e:

        print("Error generating voice:", e)
        return None