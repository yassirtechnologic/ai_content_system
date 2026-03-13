import os
import requests
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def download_images(query, output_folder, total=5):

    print("Downloading images from Pexels for:", query)

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "per_page": total
    }

    response = requests.get(url, headers=headers, params=params)

    data = response.json()

    os.makedirs(output_folder, exist_ok=True)

    images = []

    for i, photo in enumerate(data["photos"]):

        img_url = photo["src"]["large"]

        img_data = requests.get(img_url).content

        filename = f"{query.replace(' ','_')}_{i}.jpg"
        path = os.path.join(output_folder, filename)

        with open(path, "wb") as f:
            f.write(img_data)

        images.append(path)

    print("Images downloaded:", len(images))

    return images