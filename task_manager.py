def add_task(tasks, title, subject, deadline, priority, hours):
    new_id = 1
    for task in tasks:
        if task["id"] >= new_id:
            new_id = task["id"] + 1

    task = {
        "id": new_id,
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "priority": priority,
        "hours": hours,
        "completed": False,
    }
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                return False
            task["completed"] = True
            return True
    return False


def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False


def display_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available. Add a task or load demo data first.")
        return

    print("\nID  STATUS   DEADLINE    PRI  HOURS  SUBJECT        TITLE")
    print("-" * 68)
    for task in tasks:
        if task["completed"]:
            status = "DONE"
        else:
            status = "OPEN"
        deadline = task["deadline"].strftime("%Y-%m-%d")
        subject = task["subject"][:14]
        print(f"{task['id']:<3} {status:<8} {deadline:<11} {task['priority']:<4} {task['hours']:<6.1f} {subject:<14} {task['title']}")
