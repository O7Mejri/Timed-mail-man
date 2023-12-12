from send_email import sendMail

import schedule
import time
from datetime import datetimel
import os

# relative path
current_directory = os.path.dirname(__file__)
os.chdir(current_directory)



## scheduling
sched_time = "15:18"
schedule.every().day.at(sched_time).do(sendMail)

while True:
    schedule.run_pending()
    time.sleep(1)
