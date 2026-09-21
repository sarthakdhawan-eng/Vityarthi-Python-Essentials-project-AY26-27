from datetime import datetime


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def read_choice(prompt, choices):
    while True:
        value = input(prompt).strip()
        if value in choices:
            return value
        print("Invalid choice. Pick one from the menu.")


def is_valid_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def read_date(prompt):
    while True:
        value = input(prompt).strip()
        result = is_valid_date(value)
        if result is not None:
            return result
        print("Use a valid date in YYYY-MM-DD format.")


def read_priority(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and 1 <= int(value) <= 5:
            return int(value)
        print("Priority must be an integer from 1 to 5.")


def read_positive_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number > 0:
                return number
        except ValueError:
            pass
        print("Enter a number greater than 0.")


def read_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Enter a positive integer.")
