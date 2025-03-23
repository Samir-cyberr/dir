import json
import csv
import os
from abc import ABC, abstractmethod

class StorageStrategy(ABC):
    """Abstract class for different storage strategies."""
    
    @abstractmethod
    def save(self, tasks, filename):
        pass
    
    @abstractmethod
    def load(self, filename):
        pass

class CSVStorage(StorageStrategy):
    """Storage strategy for CSV format."""
    
    def save(self, tasks, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task["Task ID"], task["Title"], task["Description"], task["Due Date"], task["Status"]])
    
    def load(self, filename):
        tasks = []
        if os.path.exists(filename):
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(row)
        return tasks

class JSONStorage(StorageStrategy):
    """Storage strategy for JSON format."""
    
    def save(self, tasks, filename):
        with open(filename, 'w') as file:
            json.dump(tasks, file, indent=4)
    
    def load(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return []

class ToDoApp:
    """Main application class."""
    
    def __init__(self, storage: StorageStrategy, filename: str):
        self.storage = storage
        self.filename = filename
        self.tasks = self.storage.load(self.filename)
    
    def add_task(self, task_id, title, description, due_date, status):
        self.tasks.append({
            "Task ID": task_id,
            "Title": title,
            "Description": description,
            "Due Date": due_date,
            "Status": status
        })
        print("Task added successfully!")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(f"{task['Task ID']}, {task['Title']}, {task['Description']}, {task['Due Date']}, {task['Status']}")
    
    def update_task(self, task_id, new_title, new_description, new_due_date, new_status):
        for task in self.tasks:
            if task["Task ID"] == task_id:
                task["Title"] = new_title
                task["Description"] = new_description
                task["Due Date"] = new_due_date
                task["Status"] = new_status
                print("Task updated successfully!")
                return
        print("Task not found!")
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["Task ID"] != task_id]
        print("Task deleted successfully!")
    
    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task["Status"] == status]
        for task in filtered:
            print(f"{task['Task ID']}, {task['Title']}, {task['Description']}, {task['Due Date']}, {task['Status']}")
    
    def save_tasks(self):
        self.storage.save(self.tasks, self.filename)
        print("Tasks saved successfully!")

def main():
    storage_type = input("Choose storage format (csv/json): ").strip().lower()
    filename = "tasks." + storage_type
    storage = CSVStorage() if storage_type == "csv" else JSONStorage()
    app = ToDoApp(storage, filename)
    
    while True:
        print("""
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
        """)
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            app.add_task(task_id, title, description, due_date, status)
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID: ")
            title = input("Enter New Title: ")
            description = input("Enter New Description: ")
            due_date = input("Enter New Due Date (YYYY-MM-DD): ")
            status = input("Enter New Status (Pending/In Progress/Completed): ")
            app.update_task(task_id, title, description, due_date, status)
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            app.delete_task(task_id)
        elif choice == "5":
            status = input("Enter status to filter by (Pending/In Progress/Completed): ")
            app.filter_tasks(status)
        elif choice == "6":
            app.save_tasks()
        elif choice == "7":
            app.tasks = app.storage.load(app.filename)
            print("Tasks loaded successfully!")
        elif choice == "8":
            app.save_tasks()
            print("Exiting application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
