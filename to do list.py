import json
import os
from datetime import datetime

# File to store tasks
FILE_NAME = "tasks.json"


# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not load tasks. Starting with an empty list.")
            return []
    return []


# Save tasks to JSON file
def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Error: Unable to save tasks!")


# Add a new task
def add_task(tasks):
    title = input("Enter task name: ").strip()

    if not title:
        print("Task name cannot be empty!")
        return

    tag = input("Enter task tag (optional): ").strip()
    due_date = input("Enter due date (YYYY-MM-DD, optional): ").strip()

    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Use YYYY-MM-DD.")
            return

    task = {
        "id": max((t["id"] for t in tasks), default=0) + 1,
        "title": title,
        "completed": False,
        "tag": tag,
        "due_date": due_date
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return

    print("\n========== YOUR TASKS ==========")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(f"\nID       : {task['id']}")
        print(f"Task     : {task['title']}")
        print(f"Status   : {status}")
        print(f"Tag      : {task.get('tag', '') or 'None'}")
        print(f"Due Date : {task.get('due_date', '') or 'None'}")

    print("\n================================")


# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to mark as completed: "))
    except ValueError:
        print("Please enter a valid numeric ID!")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("Task is already completed!")
            else:
                task["completed"] = True
                save_tasks(tasks)
                print("Task marked as completed!")
            return

    print("Task ID not found!")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID!")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return

    print("Task ID not found!")


# Display menu
def display_menu():
    print("\n========== TO-DO LIST MANAGER ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("========================================")


# Main program
def main():
    tasks = load_tasks()

    print("Welcome to the To-Do List Manager!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Your tasks have been saved.")
            print("Thank you for using To-Do List Manager!")
            break

        else:
            print("Invalid choice! Please select a number from 1 to 5.")


# Run the program
if __name__ == "__main__":
    main()