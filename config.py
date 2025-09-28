# config.py
# Variables save across files if you import config
# Must import JSON on all files except config.json ofc


import json
import os

CONFIG_FILE = "config.json"

DEFAULTS = {
    "user": "guest",
    "running": True,
    "cwd": os.getcwd(),
    "playsound": 'True',
    "quickanimation": 'False',
    "fav1": 'projects/eg1',
    "fav2": 'projects/eg2',
}


# Don't touch this, gpt 5 wrote it and idk how tf it works but it does. I don't need to leave any variables though
def load():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = f.read().strip()
                if not data:  # empty file
                    return DEFAULTS.copy()
                return json.loads(data)
        except (json.JSONDecodeError, OSError):
            # corrupted file > let script overwrite
            return DEFAULTS.copy()
    return DEFAULTS.copy()

def save(state):
    with open(CONFIG_FILE, "w") as f:
        json.dump(state, f, indent=4)

state = load()
