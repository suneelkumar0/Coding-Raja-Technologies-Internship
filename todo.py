import os
import json
from datetime import datetime, timedelta

# File to store tasks
TASKS_FILE = "todo_tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
        return tasks
    else:
        return {'tasks': []}

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def display_menu():
    print("\n*** To-Do List Menu ***")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit")

def add_task(tasks):
    task_name = input("Enter task name: ")
    task_priority = input("Enter task priority (high/medium/low): ")
    due_date_input = input("Enter due date (YYYY-MM-DD, leave blank if none): ")

    if due_date_input:
        due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
    else:
        due_date = None

    tasks['tasks'].append({'name': task_name, 'priority': task_priority, 'due_date': due_date, 'completed': False})
    print("Task added successfully.")

def remove_task(tasks):
    task_index = int(input("Enter the index of the task to remove: "))
    
    if 0 <= task_index < len(tasks['tasks']):
        removed_task = tasks['tasks'].pop(task_index)
        print(f"Task '{removed_task['name']}' removed successfully.")
    else:
        print("Invalid task index.")

def mark_task_completed(tasks):
    task_index = int(input("Enter the index of the task to mark as completed: "))
    
    if 0 <= task_index < len(tasks['tasks']):
        tasks['tasks'][task_index]['completed'] = True
        print(f"Task '{tasks['tasks'][task_index]['name']}' marked as completed.")
    else:
        print("Invalid task index.")

def view_tasks(tasks):
    if not tasks['tasks']:
        print("No tasks available.")
    else:
        print("\n*** Task List ***")
        for index, task in enumerate(tasks['tasks']):
            status = "Completed" if task['completed'] else "Pending"
            due_date = task['due_date'].strftime("%Y-%m-%d") if task['due_date'] else "None"
            print(f"{index}. {task['name']} - Priority: {task['priority']}, Status: {status}, Due Date: {due_date}")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
