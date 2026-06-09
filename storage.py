import json
from pathlib import Path
from models import Alarm


DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "alarms.json"


def initialize_storage():
    """
    Creates data directory and alarms file if they don't exist.
    """
    DATA_DIR.mkdir(exist_ok=True)
    if not DATA_FILE.exists():
        with open(DATA_FILE, "w") as file:
            json.dump([], file)


def load_alarms():
    """
    Reads alarms from JSON and converts them into Alarm objects.
    """
    initialize_storage()
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        return [Alarm(**alarm) for alarm in data]

    except json.JSONDecodeError:
        print("Storage file is corrupted.")
        return []


def save_alarms(alarms):
    """
    Saves Alarm objects into JSON file.
    """
    data = [alarm.__dict__ for alarm in alarms]

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def get_next_id(alarms):
    """
    Generates next available alarm ID.
    """
    if not alarms:
        return 1

    return max(alarm.id for alarm in alarms) + 1


def add_alarm(time, label):
    """
    Creates and stores a new alarm.
    """
    alarms = load_alarms()

    alarm = Alarm(
        id=get_next_id(alarms),
        time=time,
        label=label
    )

    alarms.append(alarm)
    save_alarms(alarms)
    return alarm


def delete_alarm(alarm_id):
    """
    Deletes an alarm by ID.
    """
    alarms = load_alarms()
    updated_alarms = [
        alarm for alarm in alarms
        if alarm.id != alarm_id
    ]
    if len(updated_alarms) == len(alarms):
        return False
    save_alarms(updated_alarms)
    return True