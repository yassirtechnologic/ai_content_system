import os
import re

CALENDAR_FOLDER = "outputs/calendar"


def safe_filename(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text)
    return text[:80]


def generate_calendar(topic):

    print("Generating weekly content calendar for:", topic)

    os.makedirs(CALENDAR_FOLDER, exist_ok=True)

    calendar = f"""
WEEKLY CONTENT PLAN ABOUT: {topic}

Monday:
Market update

Tuesday:
Educational post

Wednesday:
Short video

Thursday:
Investment tips

Friday:
News analysis

Saturday:
Community engagement post

Sunday:
Weekly recap
"""

    filename = f"{safe_filename(topic)}_calendar.txt"
    filepath = os.path.join(CALENDAR_FOLDER, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(calendar)

    print("Calendar saved at:", filepath)

    return filepath