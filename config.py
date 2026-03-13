# CONFIGURATION FILE

import os

# ----------------------------
# Project settings
# ----------------------------

PROJECT_NAME = "Jorge AI Factory"

# ----------------------------
# Model configuration
# ----------------------------

MODEL_NAME = "gpt-4o-mini"

# ----------------------------
# Base path
# ----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------
# Output base folder
# ----------------------------

OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

# ----------------------------
# Content folders
# ----------------------------

SCRIPTS_FOLDER = os.path.join(OUTPUT_FOLDER, "scripts")

MUSIC_FOLDER = os.path.join(OUTPUT_FOLDER, "music")

VOICE_FOLDER = os.path.join(OUTPUT_FOLDER, "voice")

IMAGES_FOLDER = os.path.join(OUTPUT_FOLDER, "images")

VIDEOS_FOLDER = os.path.join(OUTPUT_FOLDER, "videos")

THUMBNAILS_FOLDER = os.path.join(OUTPUT_FOLDER, "thumbnails")

# ----------------------------
# Social content
# ----------------------------

POSTS_FOLDER = os.path.join(OUTPUT_FOLDER, "posts")

SHORTS_FOLDER = os.path.join(OUTPUT_FOLDER, "shorts")

IDEAS_FOLDER = os.path.join(OUTPUT_FOLDER, "ideas")

CALENDAR_FOLDER = os.path.join(OUTPUT_FOLDER, "calendar")

# ----------------------------
# Database / storage
# ----------------------------

DATABASE_FOLDER = os.path.join(BASE_DIR, "database")

CONTENT_DB = os.path.join(DATABASE_FOLDER, "content_db.json")


# ----------------------------
# Auto-create folders
# ----------------------------

FOLDERS = [
    OUTPUT_FOLDER,
    SCRIPTS_FOLDER,
    MUSIC_FOLDER,
    VOICE_FOLDER,
    IMAGES_FOLDER,
    VIDEOS_FOLDER,
    THUMBNAILS_FOLDER,
    POSTS_FOLDER,
    SHORTS_FOLDER,
    IDEAS_FOLDER,
    CALENDAR_FOLDER,
    DATABASE_FOLDER
]

for folder in FOLDERS:
    os.makedirs(folder, exist_ok=True)