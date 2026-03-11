from topic_generator import generate_topic
from translator import translate_text
from linkedin_instagram_post import generate_social_post

from script_generator import generate_script
from music_generator import generate_music
from video_generator import generate_video
from thumbnail_generator import generate_thumbnail
from shorts_generator import generate_shorts
from ideas_generator import generate_ideas
from calendar_generator import generate_calendar

from cloudinary_upload import upload_video

import os


def upload_latest_video():
    """
    Busca el último video generado en outputs/videos
    y lo sube a Cloudinary.
    """

    video_folder = "outputs/videos"

    if not os.path.exists(video_folder):
        print("Video folder not found")
        return

    videos = [os.path.join(video_folder, f) for f in os.listdir(video_folder)]

    if not videos:
        print("No videos found to upload")
        return

    latest_video = max(videos, key=os.path.getctime)

    print("Uploading video:", latest_video)

    video_url = upload_video(latest_video)

    print("Video uploaded to Cloudinary:")
    print(video_url)


def main():

    try:

        # Generate topic
        category, topic = generate_topic()
        print("\nGenerated topic:", topic)

        # Translate topic
        topic_es = translate_text(topic, "Spanish")
        topic_en = translate_text(topic, "English")

        print("\n==============================")
        print("Creating Spanish content")
        print("==============================")

        script_es = generate_script(topic_es)
        music_es = generate_music(topic_es)

        generate_video(topic_es, script_es, music_es)
        upload_latest_video()

        generate_thumbnail(topic_es)
        generate_social_post(topic_es)
        generate_shorts(topic_es)
        generate_ideas(topic_es)
        generate_calendar(topic_es)

        print("\n==============================")
        print("Creating English content")
        print("==============================")

        script_en = generate_script(topic_en)
        music_en = generate_music(topic_en)

        generate_video(topic_en, script_en, music_en)
        upload_latest_video()

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