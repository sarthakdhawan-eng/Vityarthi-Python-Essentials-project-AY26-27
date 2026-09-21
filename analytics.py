
def completion_percentage(tasks):
    if len(tasks) == 0:
        return 0
    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1
    return round((completed / len(tasks)) * 100, 1)


def subject_counts(tasks):
    counts = {}
    for task in tasks:
        subject = task["subject"]
        if subject not in counts:
            counts[subject] = 0
        counts[subject] += 1
    return counts


def show_progress(tasks):
    total = len(tasks)
    completed = 0
    pending_hours = 0
    subjects = set()

    for task in tasks:
        subjects.add(task["subject"])
        if task["completed"]:
            completed += 1
        else:
            pending_hours += task["hours"]

    print("\nPROGRESS")
    print("-" * 42)
    print(f"Total tasks      : {total}")
    print(f"Completed        : {completed}")
    print(f"Pending          : {total - completed}")
    print(f"Completion       : {completion_percentage(tasks)}%")
    print(f"Pending hours    : {pending_hours:.1f}")
    print(f"Subjects         : {len(subjects)}")

    counts = subject_counts(tasks)
    if counts:
        print("Tasks by subject:")
        for subject in sorted(counts):
            print(f"  {subject}: {counts[subject]}")
