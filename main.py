from task_manager import add_task, complete_task, delete_task, display_tasks
from planner import generate_plan
from analytics import show_progress
from validators import read_choice, read_date, read_positive_float, read_positive_int, read_priority, read_text
from demo_data import demo_tasks


def print_header():
    print("\n" + "=" * 62)
    print("FLOW - STUDENT STUDY TASK PLANNER")
    print("A task list for college study work")
    print("=" * 62)


def add_task_menu(tasks):
    print("\nADD TASK")
    title = read_text("Task title: ")
    subject = read_text("Subject: ")
    deadline = read_date("Deadline (YYYY-MM-DD): ")
    priority = read_priority("Priority (1-5): ")
    hours = read_positive_float("Estimated hours: ")
    task = add_task(tasks, title, subject, deadline, priority, hours)
    print(f"Task added with ID {task['id']}.")


def complete_task_menu(tasks):
    task_id = read_positive_int("Task ID to complete: ")
    if complete_task(tasks, task_id):
        print("Task marked as completed.")
    else:
        print("Task not found or already completed.")


def delete_task_menu(tasks):
    task_id = read_positive_int("Task ID to delete: ")
    if delete_task(tasks, task_id):
        print("Task deleted.")
    else:
        print("Task not found.")


def main():
    tasks = []
    next_id = 1
    print_header()

    while True:
        print("\nMENU")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task complete")
        print("4. Generate study plan")
        print("5. View progress")
        print("6. Load demo data")
        print("7. Delete task")
        print("0. Exit")

        choice = read_choice("Choose an option: ", ("0", "1", "2", "3", "4", "5", "6", "7"))

        if choice == "1":
            add_task_menu(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            complete_task_menu(tasks)
        elif choice == "4":
            generate_plan(tasks)
        elif choice == "5":
            show_progress(tasks)
        elif choice == "6":
            tasks.clear()
            for task in demo_tasks():
                task["id"] = next_id
                next_id += 1
                tasks.append(task)
            print("Demo data loaded.")
        elif choice == "7":
            delete_task_menu(tasks)
        else:
            print("Flow closed.")
            break


if __name__ == "__main__":
    main()
