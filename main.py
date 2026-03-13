from topic_generator import generate_topic
from translator import translate_text
from linkedin_instagram_post import generate_social_post

from script_generator import generate_script
from music_generator import generate_music
from viral_video_engine import generate_viral_video
from thumbnail_generator import generate_thumbnail
from shorts_generator import generate_shorts
from ideas_generator import generate_ideas
from calendar_generator import generate_calendar
from hook_generator import generate_hook

from cloudinary_upload import upload_video

# NUEVOS MODULOS
from image_generator import download_images
from voice_generator import generate_voice

# CONFIG
from config import IMAGES_FOLDER, VOICE_FOLDER


def main():

    try:

        # ----------------------------
        # Generate topic
        # ----------------------------

        category, topic = generate_topic()

        hook = generate_hook(topic)

        print("\nGenerated topic:", topic)

        # ----------------------------
        # Translate topic
        # ----------------------------

        topic_es = translate_text(topic, "Spanish")
        topic_en = translate_text(topic, "English")

        # ============================
        # SPANISH CONTENT
        # ============================

        print("\n==============================")
        print("Creating Spanish content")
        print("==============================")

        # Script
        script_es = generate_script(hook + ". " + topic_es)

        # Voice
        voice_es = generate_voice(script_es, topic_es)

        # Images
        images_es = download_images(topic_es, IMAGES_FOLDER)

        # Music
        music_es = generate_music(topic_es)

        # Video
        video_es = generate_viral_video(
            topic_es,
            script_es,
            images_es,
            voice_es,
            music_es
        )

        # Upload
        print("Uploading video:", video_es)
        upload_video(video_es, topic_es)

        # Extra content
        generate_thumbnail(topic_es)
        generate_social_post(topic_es)
        generate_shorts(topic_es)
        generate_ideas(topic_es)
        generate_calendar(topic_es)

        # ============================
        # ENGLISH CONTENT
        # ============================

        print("\n==============================")
        print("Creating English content")
        print("==============================")

        # Script
        script_en = generate_script(hook + ". " + topic_en)

        # Voice
        voice_en = generate_voice(script_en, topic_en)

        # Images
        images_en = download_images(topic_en, IMAGES_FOLDER)

        # Music
        music_en = generate_music(topic_en)

        # Video
        video_en = generate_viral_video(
            topic_en,
            script_en,
            images_en,
            voice_en,
            music_en
        )

        # Upload
        print("Uploading video:", video_en)
        upload_video(video_en, topic_en)

        # Extra content
        generate_thumbnail(topic_en)
        generate_social_post(topic_en)
        generate_shorts(topic_en)
        generate_ideas(topic_en)
        generate_calendar(topic_en)

        print("\n==============================")
        print("AI CONTENT SYSTEM COMPLETE")
        print("==============================")

    except Exception as e:

        print("\nERROR OCCURRED:")
        print(e)


if __name__ == "__main__":
    main()