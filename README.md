# Timed Mail Man

## Project Overview
Timed Mail Man is a Python project that sends emails on schedule. It allows you to automate the sending of emails at specified intervals, making it useful for various automated communication scenarios.

## Running Indefinitely

### Option 1: Visual Studio Code
You can run your script directly in VSCode, and it will keep running until you manually stop it.
- Open your script in VSCode.
- Use the "Run Python File in Terminal" option (usually by right-clicking on the script and selecting it).

### Option 2: Command Line
Open a terminal or command prompt and navigate to the directory where your script is located.

    python send_email.py

### Option 3: Background Process
You can run your script as a background process to detach it from the terminal.

On Unix-based Systems

    nohup python send_email.py &

On Windows

    start python send_email.py

To close it: Using taskkill Command:
Open a new Command Prompt window.
Use the tasklist command to find the process ID (PID) of the Python process:

    tasklist | find "python"
    
Look for the entry related to your script and note its PID.
Use the taskkill command to terminate the process using its PID:

    taskkill /F /PID <PID>

### Using Scheduling Services

1. Windows Task Scheduler
Description: Windows Task Scheduler is a built-in task scheduling application in Microsoft Windows. It allows you to schedule tasks to run at specific times or events.
How to Use: Create a task in Windows Task Scheduler that runs your Python script at the desired time. Set the trigger to daily at 8 am, for example.

2. Cron (Unix-based Systems)
Description: Cron is a time-based job scheduler in Unix-like operating systems. It allows you to schedule tasks to run at specific intervals.
How to Use: Add an entry to the crontab file to schedule your Python script. For example, to run the script every day at 8 am:

    ```bash
    0 8 * * * /path/to/python /path/to/send_email.py

### Other Services
If you don't have access to a dedicated server or always-on machine and want a free solution to schedule your script, consider the following services:

1. Google Colab:
Upload your script to Google Colab and use Colab's runtime scheduling feature to run it at specific intervals.
2. GitHub Actions:
Use GitHub Actions to schedule the execution of your script. Create a GitHub repository, add your script, and set up a workflow with a scheduled trigger.
3. Heroku (Free Tier):
Heroku allows you to deploy and run Python scripts. You can use the free tier, but note that there might be limitations on the number of hours your application can run per day.







