from datetime import date


def urgency_score(deadline, today=None):
    if today is None:
        today = date.today()

    days_left = (deadline - today).days

    if days_left <= 0:
        return 100
    if days_left == 1:
        return 90
    if days_left <= 3:
        return 75
    if days_left <= 7:
        return 55
    if days_left <= 14:
        return 35
    return 15


def priority_score(task, today=None):
    urgency = urgency_score(task["deadline"], today)
    academic = task["priority"] * 20
    effort = max(0, 100 - int(task["hours"] * 10))
    return round((urgency * 0.50) + (academic * 0.30) + (effort * 0.20), 2)


def selection_sort(tasks, today=None):
    result = tasks[:]

    for i in range(len(result) - 1):
        best = i
        for j in range(i + 1, len(result)):
            current_score = priority_score(result[j], today)
            best_score = priority_score(result[best], today)
            if current_score > best_score:
                best = j
        result[i], result[best] = result[best], result[i]

    return result


def explain(task, today=None):
    if today is None:
        today = date.today()
    days_left = (task["deadline"] - today).days
    if days_left <= 0:
        return "Due today or overdue."
    if days_left == 1:
        return "Due tomorrow."
    if task["priority"] >= 4:
        return "High academic priority."
    if task["hours"] <= 2:
        return "Small task that can be finished quickly."
    return "A mix of deadline, priority, and effort."


def generate_plan(tasks):
    pending = []
    for task in tasks:
        if not task["completed"]:
            pending.append(task)

    if not pending:
        print("\nNo pending tasks.")
        return

    ranked = selection_sort(pending)
    print("\nSTUDY PLAN")
    print("-" * 72)

    limit = min(5, len(ranked))
    for position in range(limit):
        task = ranked[position]
        score = priority_score(task)
        print(f"{position + 1}. {task['title']}  |  Score: {score}")
        print(f"   {task['subject']} | Due: {task['deadline'].isoformat()} | "
              f"Priority: {task['priority']}/5 | {task['hours']:.1f}h")
        print(f"   Reason: {explain(task)}")
