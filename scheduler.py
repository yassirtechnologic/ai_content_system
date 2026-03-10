import schedule
import time
from main import main

schedule.every().monday.at("09:00").do(main)
schedule.every().wednesday.at("09:00").do(main)
schedule.every().friday.at("09:00").do(main)

print("AI Content Scheduler Running...")

while True:
    schedule.run_pending()
    time.sleep(60)