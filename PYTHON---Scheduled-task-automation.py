import schedule
import time
import subprocess
from datetime import datetime

def task_example():
    print(f"Task executed at {datetime.now()}")
    
    # Example: Run a script
    subprocess.run(["python", "example_script.py"])

def backup_task():
    print(f"Backup started at {datetime.now()}")
    subprocess.run(["tar", "-czf", "backup.tar.gz", "./important_folder"])

def email_task():
    print(f"Sending email at {datetime.now()}")
    # Example: Simulate sending an email
    subprocess.run(["echo", "Email sent successfully!"])

# Schedule tasks
schedule.every(10).seconds.do(task_example)
schedule.every().day.at("12:00").do(backup_task)
schedule.every().monday.at("08:00").do(email_task)

print("Task automation started...")
while True:
    schedule.run_pending()
    time.sleep(1)
