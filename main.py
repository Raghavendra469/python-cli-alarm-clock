from cli import create_parser
from storage import (
    add_alarm,
    delete_alarm,
    load_alarms
)
from utils import validate_time
from scheduler import run_scheduler


def list_alarms():

    alarms = load_alarms()

    if not alarms:
        print("No alarms found.")
        return

    print()
    print(f"{'ID':<5} {'TIME':<10} LABEL")
    print("-" * 40)

    for alarm in alarms:
        print(
            f"{alarm.id:<5} "
            f"{alarm.time:<10} "
            f"{alarm.label}"
        )


def main():

    parser = create_parser()

    args = parser.parse_args()

    if args.command == "add":

        if not validate_time(args.time):
            print("Invalid time format. Use HH:MM")
            return

        alarm = add_alarm(
            args.time,
            args.label
        )

        print(
            f"Alarm added successfully "
            f"(ID: {alarm.id})"
        )

    elif args.command == "list":

        list_alarms()

    elif args.command == "delete":

        success = delete_alarm(args.id)

        if success:
            print("Alarm deleted.")
        else:
            print("Alarm not found.")

    elif args.command == "run":

        run_scheduler()

    else:

        parser.print_help()


if __name__ == "__main__":
    main()