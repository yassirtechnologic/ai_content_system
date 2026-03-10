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
# Output folders
# ----------------------------

OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

SCRIPTS_FOLDER = os.path.join(OUTPUT_FOLDER, "scripts")
MUSIC_FOLDER = os.path.join(OUTPUT_FOLDER, "music")
VIDEOS_FOLDER = os.path.join(OUTPUT_FOLDER, "videos")
THUMBNAILS_FOLDER = os.path.join(OUTPUT_FOLDER, "thumbnails")
POSTS_FOLDER = os.path.join(OUTPUT_FOLDER, "posts")
SHORTS_FOLDER = os.path.join(OUTPUT_FOLDER, "shorts")
IDEAS_FOLDER = os.path.join(OUTPUT_FOLDER, "ideas")
CALENDAR_FOLDER = os.path.join(OUTPUT_FOLDER, "calendar")