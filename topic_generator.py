import random

CATEGORIES = {

    "ai_technology": [
        "How AI automates small businesses",
        "Top AI tools entrepreneurs should use",
        "AI workflows that save hours every week",
        "How artificial intelligence is changing work",
        "The future of AI in business"
    ],

    "business_automation": [
        "Why every business needs a chatbot",
        "How automation increases customer responses",
        "How technology helps small businesses grow",
        "How to automate repetitive business tasks",
        "How AI can save hours of work every week"
    ]

}

def generate_topic():

    category = random.choice(list(CATEGORIES.keys()))
    topic = random.choice(CATEGORIES[category])

    return category, topic