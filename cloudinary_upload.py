import cloudinary
import cloudinary.uploader
import os

from content_storage import save_video
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)


def upload_video(file_path, topic):

    try:

        # Verificar que el archivo existe
        if not os.path.exists(file_path):
            print("ERROR: Video file not found:", file_path)
            return None

        # Verificar tamaño
        file_size = os.path.getsize(file_path)
        print("Video size:", file_size)

        if file_size == 0:
            print("ERROR: video file is empty")
            return None

        print("Uploading video to Cloudinary:")
        print(file_path)

        # Subir video
        result = cloudinary.uploader.upload(
            file_path,
            resource_type="video",
            chunk_size=6000000,
            format="mp4"
        )

        video_url = result.get("secure_url")

        print("Video uploaded successfully!")
        print("Cloudinary URL:", video_url)

        # GUARDAR EN LA BASE DE DATOS
        save_video(topic, video_url)

        print("Video saved to content database")

        return video_url

    except Exception as e:

        print("Cloudinary upload error:")
        print(str(e))

        return None