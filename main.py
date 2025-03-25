import os
import requests
import time

from dotenv import load_dotenv

import discordrpc
from discordrpc.button import Button

load_dotenv()

CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
PROJECT_ID = os.getenv("PROJECT_ID")
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL")) or 300

if not CLIENT_ID:
    raise ValueError("DISCORD_CLIENT_ID not found in environment variables (Check your .env file)!")

if not PROJECT_ID:
    raise ValueError("PROJECT_ID not found in environment variables (Check your .env file)!")

API_URL = "https://1001albumsgenerator.com/api/v1/projects/"

# Determines which of 3 (0-2) images from the 1001Albums API to send to Discord.
# 0 = Small, 1 = Medium, 2 = Large
IMAGE_SIZE_SELECTION = 1

rpc_data_old = {
    # <full_name>, <artwork_url>, <total_str>
}

def updateRPC(rpc_data):
    name, artwork_url, total_albums_str = rpc_data

    button = Button(
        button_one_label="My Summary",
        button_one_url="https://1001albumsgenerator.com/shares/" + PROJECT_ID,
        button_two_label="Project GitHub",
        button_two_url="https://github.com/snepderg"
    )

    rpc.set_activity(
        details=name,
        state=f"• Total Albums: [{total_albums_str}]",
        buttons=button,
        large_image=artwork_url,
        large_text=name,
        )

# Query 1001Albums
# https://1001albumsgenerator.com/api/v1/projects/:ProjectID
def fetch_api_data():
    try:
        response = requests.get(API_URL + PROJECT_ID)
        if response.status_code == 200:
            return  response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

def update():
    global rpc_data_old
    rpc_data = []

    api_data = fetch_api_data()
    history = api_data["history"]

    album = None
    index = -1  # Default to -1 if history is empty

    for i, target in enumerate(history):
        if "rating" not in target:
            album = target["album"]
            index = i
            break

    if album is None and history:
        album = history[-1]
        index = len(history) - 1

    full_name = album["name"] + " - " + album["artist"]
    artwork_url = album["images"][IMAGE_SIZE_SELECTION]["url"]  # 2nd image (medium)
    total_albums = f"{index + 1}/{len(history)}"

    rpc_data = [full_name, artwork_url, total_albums]

    if rpc_data != rpc_data_old:
        updateRPC(rpc_data)
        rpc_data_old = rpc_data


    full_name = album["name"] + " - " + album["artist"]
    artwork_url = album["images"][IMAGE_SIZE_SELECTION]["url"] # 2nd image (medium)
    total_albums_str = f"{index + 1}/{len(history)}"

    rpc_data.append(full_name)
    rpc_data.append(artwork_url)
    rpc_data.append(total_albums_str)

    if rpc_data != rpc_data_old:
        updateRPC(rpc_data)
        rpc_data_old = rpc_data

if __name__ == "__main__":
    print("1001 Albums RPC by Snepderg")
    print(f"Call interval set to: {str(UPDATE_INTERVAL / 60)} minutes!")

    rpc = discordrpc.RPC(app_id=CLIENT_ID)

    while True:
        update()
        time.sleep(UPDATE_INTERVAL)