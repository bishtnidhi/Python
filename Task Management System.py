import json
import os
from datetime import datetime

# Task class to represent a single task
class Task:
    def __init__(self, title, description, category, due_date):
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.status = "Pending"

    def mark_completed(self):
        self.status = "Completed"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nCategory: {self.category}\nDue Date: {self.due_date}\nStatus: {self.status}"

# TaskManager class to manage all tasks
class TaskManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return [Task(**task) for task in json.load(file)]
        return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def add_task(self, title, description, category, due_date):
        task = Task(title, description, category, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self, filter_by=None):
        filtered_tasks = self.tasks
        if filter_by:
            filtered_tasks = [task for task in self.tasks if task.status == filter_by]
        if not filtered_tasks:
            print("No tasks found.")
        for task in filtered_tasks:
            print("\n" + str(task) + "\n")

    def update_task(self, task_index, title=None, description=None, category=None, due_date=None):
        task = self.tasks[task_index]
        if title: task.title = title
        if description: task.description = description
        if category: task.category = category
        if due_date: task.due_date = due_date
        self.save_tasks()

    def delete_task(self, task_index):
        del self.tasks[task_index]
        self.save_tasks()

    def mark_completed(self, task_index):
        self.tasks[task_index].mark_completed()
        self.save_tasks()

# Function to interact with the user
def main():
    manager = TaskManager('tasks.json')

    while True:
        print("\n=== Task Management System ===")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. List Completed Tasks")
        print("4. List Pending Tasks")
        print("5. Update Task")
        print("6. Delete Task")
        print("7. Mark Task as Completed")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (e.g., Work, Personal): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
                manager.add_task(title, description, category, due_date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            manager.list_tasks(filter_by="Completed")
        elif choice == '4':
            manager.list_tasks(filter_by="Pending")
        elif choice == '5':
            task_index = int(input("Enter task index to update: "))
            if 0 <= task_index < len(manager.tasks):
                title = input("Enter new title (leave blank to keep current): ")
                description = input("Enter new description (leave blank to keep current): ")
                category = input("Enter new category (leave blank to keep current): ")
                due_date = input("Enter new due date (leave blank to keep current, format YYYY-MM-DD): ")
                if due_date == "":
                    due_date = None
                try:
                    if due_date:
                        datetime.strptime(due_date, '%Y-%m-%d')
                    manager.update_task(task_index, title, description, category, due_date)
                except ValueError:
                    if due_date:
                        print("Invalid date format. Please use YYYY-MM-DD.")
            else:
                print("Invalid task index.")
        elif choice == '6':
            task_index = int(input("Enter task index to delete: "))
            if 0 <= task_index < len(manager.tasks):
                manager.delete_task(task_index)
            else:
                print("Invalid task index.")
        elif choice == '7':
            task_index = int(input("Enter task index to mark as completed: "))
            if 0 <= task_index < len(manager.tasks):
                manager.mark_completed(task_index)
            else:
                print("Invalid task index.")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
