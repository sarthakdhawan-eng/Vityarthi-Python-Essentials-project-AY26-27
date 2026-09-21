# Flow - Student Study Task Planner

## Overview

Flow is a small command-line Python program for college students. It helps a student record study tasks, mark work as completed, see progress, and create a simple study order based on deadline, priority, and estimated effort.

The project is intentionally built with the basic Python and problem-solving concepts covered in **CSE1021 - Introduction to Problem Solving and Programming**.

## Main Features

1. **Task Management** - add, view, complete, and delete tasks.
2. **Study Planner** - calculate a transparent priority score and arrange pending tasks using selection sort.
3. **Progress Analysis** - calculate completion percentage, pending study hours, subject counts, and number of subjects.
4. **Demo Data** - load sample tasks for quick demonstration.

## Course Concepts Used

| Course concept | Where it is used |
|---|---|
| Problem decomposition | Separate modules for tasks, planning, validation, and analysis |
| Functions and modules | Every feature is divided into small functions |
| Lists | Tasks are stored as a list of dictionaries |
| Dictionaries | Each task stores related values using key-value pairs |
| Tuples | Menu choices are validated against a tuple of options |
| Sets | Unique subjects are found in the progress module |
| Conditionals | Input validation and priority rules |
| Loops | Menu loop, task search, counting, sorting |
| Break / program termination | Main menu exits with a controlled `break` |
| Array/list algorithms | Selection sort is implemented manually |
| Time-effort trade-off | Study-plan score includes estimated effort |

## Functional Modules

### 1. Task Management
Input: title, subject, deadline, priority, estimated hours.

Output: stored task list, completion status, or deletion result.

### 2. Study Planner
Input: pending tasks.

Processing: calculate urgency, combine three factors into a score, and use selection sort.

Output: ranked study plan with a short reason for each task.

### 3. Progress Analysis
Input: current task list.

Processing: counting, percentage calculation, dictionary-based subject counting, and set-based unique subject detection.

Output: progress summary.

## Non-Functional Requirements

1. **Performance:** operations should respond immediately for a normal student-sized list of tasks.
2. **Usability:** menu options and input formats are printed clearly.
3. **Reliability:** invalid values are checked before they are accepted.
4. **Maintainability:** each major feature has its own module and simple functions.
5. **Portability:** only Python's standard library is required.

## Project Structure

```text
Flow_Project/
├── main.py
├── task_manager.py
├── planner.py
├── analytics.py
├── validators.py
├── demo_data.py
├── requirements.txt
├── statement.md
├── tests/
│   └── test_flow.py
├── docs/
│   ├── design.md
│   └── diagrams/
└── report/
    └── project_report.pdf
```

## Requirements

- Python 3.10 or later
- No third-party packages

## Run the Project

Open a terminal in the project folder:

```bash
python main.py
```

For a quick demonstration:

```text
6 -> Load demo data
4 -> Generate study plan
5 -> View progress
2 -> View tasks
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Study Plan Formula

```text
Score = 0.50 × Urgency + 0.30 × Academic Priority + 0.20 × Effort Score
```

The score is rule-based and deterministic. It is included to demonstrate decomposition, conditionals, arithmetic expressions, and an algorithm for ordering a list.

## Design Documents

The `docs` folder contains:

- problem-solving/design notes
- pseudocode
- architecture diagram
- workflow diagram
- use case diagram
- sequence diagram
- component diagram

**No database is used, so an ER diagram is not required for this version.**

## Author

**Sarthak**
B.Tech CSE (Artificial Intelligence and Machine Learning)
VIT