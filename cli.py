import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="CLI Alarm Clock"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # Add alarm
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new alarm"
    )

    add_parser.add_argument(
        "time",
        help="Alarm time in HH:MM format"
    )

    add_parser.add_argument(
        "--label",
        default="Alarm",
        help="Alarm label"
    )

    # List alarms
    subparsers.add_parser(
        "list",
        help="List all alarms"
    )

    # Delete alarm
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete an alarm"
    )

    delete_parser.add_argument(
        "id",
        type=int,
        help="Alarm ID"
    )

    # Run scheduler
    subparsers.add_parser(
        "run",
        help="Start alarm scheduler"
    )

    return parser