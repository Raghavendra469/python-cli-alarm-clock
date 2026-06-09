from datetime import datetime


def validate_time(time_str):
    """
    Validate HH:MM format.
    """

    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def get_current_time():
    """
    Returns current time in HH:MM.
    """

    return datetime.now().strftime("%H:%M")


def is_alarm_due(alarm_time):
    """
    Returns True if alarm should trigger.
    """

    return alarm_time == get_current_time()