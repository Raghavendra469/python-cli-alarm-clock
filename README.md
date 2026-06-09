# Python CLI Alarm Clock

## Overview

This project is a Python-based Command Line Interface (CLI) Alarm Clock application built as part of a take-home engineering exercise.

The requirements were intentionally open-ended, so before implementation I focused on defining a realistic MVP, identifying edge cases, designing a maintainable architecture, and documenting engineering trade-offs.

The application allows users to:

* Add alarms
* List alarms
* Delete alarms
* Persist alarms between application runs
* Run a scheduler that triggers alarms at the configured time

The project uses only Python standard library modules and does not require a database or external services.

---

## Requirement Refinement

Since the task did not provide a detailed specification, I first defined the following MVP requirements.

### Included Features

* Add alarm
* List alarms
* Delete alarm
* Run alarm scheduler
* JSON-based persistence
* Input validation

### Out of Scope

To keep the implementation focused and maintainable, I intentionally excluded:

* GUI/Web UI
* Database integration
* Cloud synchronization
* Time zone management

---

## Project Structure

```text
alarm-clock/
│
├── main.py
├── cli.py
├── models.py
├── storage.py
├── scheduler.py
├── utils.py
│
├── data/
│   └── alarms.json
│
└── README.md
```

### File Responsibilities

#### main.py

Application entry point.

Responsible for:

* Processing parsed commands
* Coordinating different modules
* Executing user actions

#### cli.py

Handles command-line argument parsing using argparse.

Supported commands:

```bash
python main.py add 07:30 --label Gym
python main.py list
python main.py delete 1
python main.py run
```

#### models.py

Contains the Alarm data model.

#### storage.py

Responsible for:

* Reading alarms from JSON
* Writing alarms to JSON
* Creating alarm IDs
* Adding and deleting alarms

#### scheduler.py

Runs the alarm monitoring loop and triggers alarms when due.

#### utils.py

Contains reusable helper functions such as:

* Time validation
* Time comparison
* Date/time utilities

---

Sample testing Commands: 

python main.py add 07:30 --label Gym,

python main.py list,

python main.py run,

python main.py delete 1 (1 indicated the id of alarm)
