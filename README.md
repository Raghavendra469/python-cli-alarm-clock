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
## Design Decisions

### Why JSON Instead of a Database?

The exercise explicitly stated that a database was not required.

JSON was chosen because it is:

* Lightweight
* Human-readable
* Easy to debug
* Sufficient for a single-user CLI application

Example:

```json
[
  {
    "id": 1,
    "time": "07:30",
    "label": "Gym"
  }
]
```

---

### Why argparse?

argparse is part of Python's standard library and provides:

* Structured command handling
* Automatic help generation
* Input validation
* Good CLI user experience

---

### Why Separate Modules?

I separated responsibilities into dedicated modules to improve maintainability and readability.

Benefits:

* Easier testing
* Better separation of concerns
* Simpler future enhancements
* Reduced coupling between components

---

### Why Poll Every Second?

The scheduler checks alarms once per second.

This approach was chosen because:

* It is simple to understand
* Reliable for an alarm clock use case
* Avoids unnecessary complexity

For a small CLI application, this trade-off is acceptable.

---

## Edge Cases Considered

### Invalid Time Format

Example:

```bash
python main.py add 25:99
```

Result:

```text
Invalid time format. Use HH:MM
```

---

### Empty Alarm Storage

If no alarms exist:

```bash
python main.py list
```

Result:

```text
No alarms found.
```

---

### Invalid Alarm ID

Example:

```bash
python main.py delete 100
```

Result:

```text
Alarm not found.
```

---

### Corrupted JSON Storage

If the JSON file is corrupted, the application handles the error gracefully rather than crashing.

---

## How to Run

### Add Alarm

```bash
python main.py add 07:30 --label Gym
```

### List Alarms

```bash
python main.py list
```

### Delete Alarm

```bash
python main.py delete 1
```

### Start Scheduler

```bash
python main.py run
```

---
## AI-Assisted Development Process

As requested in the exercise, AI was used during the planning and design phases.

AI was used to:

* Refine requirements from the open-ended prompt
* Brainstorm edge cases
* Review architectural options
* Suggest project structure
* Identify validation scenarios

All generated suggestions were reviewed before implementation.

Several proposed features were intentionally rejected, including:

* Relative alarms
* Recurring alarms
* Snooze functionality
* Desktop notifications

These features were excluded to maintain a focused MVP and ensure a clean, reliable implementation within the scope of the exercise.

-------------------------------------------------------------------------------

Sample testing Commands: 

python main.py add 07:30 --label Gym,

python main.py list,

python main.py run,

python main.py delete 1 (1 indicated the id of alarm)
