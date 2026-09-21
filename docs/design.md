# Flow - Design Notes

## 1. Problem-Solving Approach

The problem is divided into three main parts:

1. Manage the task list.
2. Decide the order of pending tasks.
3. Measure progress.

Each part is implemented as a separate module. This follows top-down design and keeps functions small enough to test.

## 2. Data Representation

A task is stored as a dictionary:

```text
{
  id, title, subject, deadline, priority, hours, completed
}
```

All tasks are stored in a Python list.

A set is used for unique subjects, and a dictionary is used for subject-wise counts.

## 3. Study-Plan Algorithm

For each pending task:

```text
1. Find days left until deadline.
2. Convert days left into an urgency score.
3. Convert priority 1-5 into a 20-100 academic score.
4. Convert estimated hours into an effort score.
5. Calculate the weighted total.
6. Use selection sort to arrange tasks from highest score to lowest.
```

### Pseudocode

```text
START
GET pending tasks
FOR each task
    calculate urgency
    calculate academic priority
    calculate effort score
    total = weighted sum of three scores
END FOR
selection sort tasks by total score
DISPLAY top five tasks
STOP
```

## 4. Architecture

```text
User
  |
  v
main.py
  |
  +--> validators.py
  |
  +--> task_manager.py
  |
  +--> planner.py
  |
  +--> analytics.py
  |
  +--> demo_data.py
```

## 5. Non-Functional Requirements

- Performance: quick response for normal task lists.
- Usability: numbered menu and clear prompts.
- Reliability: repeated validation loops prevent invalid input.
- Maintainability: one clear responsibility per module.
- Portability: standard Python library only.

## 6. Error Handling

The program checks empty text, date format, priority range, positive numeric input, and menu choices. Invalid input shows a message and asks again.

## 7. Testing

The test file checks task creation, completion/deletion, priority scoring, selection sort, analytics, and date validation.
