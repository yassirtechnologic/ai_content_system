import cloudinary
import cloudinary.uploader
import os


# Configuración de Cloudinary usando variables de entorno
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)


def upload_video(file_path):
    """
    Uploads a video file to Cloudinary and returns the public URL
    """

    try:

        # Verificar que el archivo existe
        if not os.path.exists(file_path):
            print("ERROR: Video file not found:", file_path)
            return None

        print("Uploading video to Cloudinary:")
        print(file_path)

        result = cloudinary.uploader.upload(
            file_path,
            resource_type="video"
        )

        video_url = result.get("secure_url")

        print("Video uploaded successfully!")
        print("Cloudinary URL:", video_url)

        return video_url

    except Exception as e:

        print("Cloudinary upload error:")
        print(str(e))

        return None