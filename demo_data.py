from datetime import date, timedelta


def demo_tasks():
    today = date.today()
    return [
        {"id": 0, "title": "Python lab", "subject": "Programming", "deadline": today + timedelta(days=1), "priority": 5, "hours": 2.0, "completed": False},
        {"id": 0, "title": "Calculus practice", "subject": "Mathematics", "deadline": today + timedelta(days=3), "priority": 4, "hours": 2.5, "completed": False},
        {"id": 0, "title": "Physics revision", "subject": "Physics", "deadline": today + timedelta(days=7), "priority": 3, "hours": 3.0, "completed": False},
        {"id": 0, "title": "English notes", "subject": "English", "deadline": today + timedelta(days=10), "priority": 2, "hours": 1.0, "completed": False},
    ]
