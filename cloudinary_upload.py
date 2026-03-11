import cloudinary
import cloudinary.uploader
import os


cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)


def upload_video(file_path):

    try:

        print("Uploading video:", file_path)

        result = cloudinary.uploader.upload(
            file_path,
            resource_type="video"
        )

        video_url = result["secure_url"]

        print("Video uploaded successfully:")
        print(video_url)

        return video_url

    except Exception as e:

        print("Cloudinary upload error:")
        print(e)

        return None