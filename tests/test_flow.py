import unittest
from datetime import date, timedelta

from task_manager import add_task, complete_task, delete_task
from planner import priority_score, selection_sort
from analytics import completion_percentage, subject_counts
from validators import is_valid_date


class FlowTests(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        task = add_task(tasks, "Math", "Mathematics", date.today(), 5, 2)
        self.assertEqual(task["id"], 1)
        self.assertEqual(len(tasks), 1)

    def test_complete_and_delete(self):
        tasks = []
        add_task(tasks, "Lab", "Programming", date.today(), 4, 1)
        self.assertTrue(complete_task(tasks, 1))
        self.assertTrue(tasks[0]["completed"])
        self.assertTrue(delete_task(tasks, 1))
        self.assertEqual(len(tasks), 0)

    def test_priority_score(self):
        urgent = {"deadline": date.today(), "priority": 3, "hours": 2}
        later = {"deadline": date.today() + timedelta(days=14), "priority": 3, "hours": 2}
        self.assertGreater(priority_score(urgent), priority_score(later))

    def test_selection_sort(self):
        tasks = [
            {"id": 1, "deadline": date.today() + timedelta(days=14), "priority": 2, "hours": 2},
            {"id": 2, "deadline": date.today(), "priority": 5, "hours": 1},
        ]
        ranked = selection_sort(tasks)
        self.assertEqual(ranked[0]["id"], 2)

    def test_analytics_and_validation(self):
        tasks = [
            {"subject": "Math", "completed": True},
            {"subject": "Programming", "completed": False},
        ]
        self.assertEqual(completion_percentage(tasks), 50.0)
        self.assertEqual(subject_counts(tasks)["Math"], 1)
        self.assertIsNotNone(is_valid_date("2026-09-21"))
        self.assertIsNone(is_valid_date("21-09-2026"))


if __name__ == "__main__":
    unittest.main()
