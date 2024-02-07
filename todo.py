import json
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, description, priority, due_date):
    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task removed: {removed_task['description']}")
    else:
        print("Invalid task index")

def mark_task_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i + 1}. {task['description']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, description, priority, due_date)
        elif choice == '2':
            index = int(input("Enter task index to remove: ")) - 1
            remove_task(tasks, index)
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: ")) - 1
            mark_task_completed(tasks, index)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()