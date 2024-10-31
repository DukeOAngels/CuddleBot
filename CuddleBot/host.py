import os
import requests
import base64
import json
import time
from datetime import datetime
import pytz
import socket

UPDATE_INTERVAL = 10  
GITHUB_TOKEN_PATH = 'Cuddlebot/GITHUB_TOKEN.txt'
REPO_OWNER = 'DukeOAngels' 
REPO_NAME = 'CuddleBot'     
RUNTIME_FILE_PATH = 'CuddleBot/runtime.txt'
BRANCH = 'main'         

def load_token(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        return file.read().strip()

TOKEN = load_token(GITHUB_TOKEN_PATH)

def update_runtime_file(status, crash_time=None, run_duration=None):
    log_message = ""
    if status == "running":
        log_message = "Host Monitor Status: running\n"
    elif status == "crashed":
        log_message = f"Crash: {crash_time}\nRunned for: {run_duration}\n"

    with open(RUNTIME_FILE_PATH, 'a') as file:
        file.write(log_message)

    update_file_on_github(RUNTIME_FILE_PATH, 'CuddleBot/runtime.txt')

def update_file_on_github(file_path, file_name):
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            new_content = file.read()
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    encoded_content = base64.b64encode(new_content.encode()).decode()
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_name}?ref={BRANCH}'
    headers = {
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_info = response.json()
        sha = file_info['sha']

        update_url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_name}'
        data = {
            'message': f'Updating {file_name}',
            'content': encoded_content,
            'sha': sha,
            'branch': BRANCH,
        }

        update_response = requests.put(update_url, headers=headers, data=json.dumps(data))
        
        if update_response.status_code == 200:
            print(f"{file_name} updated successfully on GitHub.")
        else:
            print(f"Error updating {file_name} on GitHub:", update_response.json())
    else:
        print(f"Error fetching file information for {file_name}:", response.json())

status = "unknown" 
start_time = datetime.now(pytz.timezone('UTC'))

while True:
    try:
        with socket.create_connection(('localhost', 12345), timeout=1):
            current_status = "running"
            if status != current_status:
                crash_time = None
                run_duration = None
                update_runtime_file(current_status)  # Log running status
                print("main.py is running.")
                status = current_status
                
                update_file_on_github('CuddleBot/main.py', 'CuddleBot/main.py')
                update_file_on_github('CuddleBot/host.py', 'CuddleBot/host.py')  
    except (ConnectionRefusedError, OSError):
        crash_time = datetime.now(pytz.timezone('UTC')).strftime('%Y-%m-%d %H:%M:%S %Z')

        end_time = datetime.now(pytz.timezone('UTC'))
        run_duration = end_time - start_time
        
        days, remainder = divmod(run_duration.total_seconds(), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        formatted_duration = f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
        
        current_status = "crashed"
        if status != current_status:
            update_runtime_file(current_status, crash_time, formatted_duration) 
            print("main.py has stopped running.")
            status = current_status

    time.sleep(UPDATE_INTERVAL) 
