import time

from storage import load_alarms
from utils import is_alarm_due


triggered_alarms = set()


def ring_alarm(alarm):
    """
    Display alarm notification.
    """

    print("\n" + "=" * 50)
    print("⏰ ALARM TRIGGERED")
    print(f"Label : {alarm.label}")
    print(f"Time  : {alarm.time}")
    print("=" * 50)

    print("\a")  # terminal bell


def run_scheduler():
    """
    Runs continuously and checks alarms.
    """

    print("Alarm scheduler started...")
    print("Press Ctrl+C to stop.\n")

    try:

        while True:

            alarms = load_alarms()

            for alarm in alarms:

                key = (alarm.id, alarm.time)

                if is_alarm_due(alarm.time):

                    if key not in triggered_alarms:
                        ring_alarm(alarm)
                        triggered_alarms.add(key)

            time.sleep(1)

    except KeyboardInterrupt:

        print("\nScheduler stopped.")