import json
import csv

def load_tasks():
    with open('tasks.json', 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\nTask List:")
    print("{:<5} {:<20} {:<10} {:<8}".format("ID", "Task Name", "Completed", "Priority"))
    print("-" * 45)
    for task in tasks:
        print("{:<5} {:<20} {:<10} {:<8}".format(
            task['id'], 
            task['task'], 
            str(task['completed']), 
            task['priority']
        ))

def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task['completed'])
    pending = total - completed
    avg_priority = sum(task['priority'] for task in tasks) / total if total > 0 else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {avg_priority:.1f}")

def convert_to_csv(tasks):
    with open('tasks.csv', 'w', newline='') as file:
        fieldnames = ['ID', 'Task', 'Completed', 'Priority']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })
    
    print("\nTasks data has been converted to tasks.csv")

def main():
    # Load tasks
    tasks = load_tasks()
    
    # Display tasks
    display_tasks(tasks)
    
    # Calculate and display stats
    calculate_stats(tasks)
    
    # Example of modifying a task
    if tasks:
        tasks[0]['completed'] = True
        save_tasks(tasks)
        print("\nMarked first task as completed and saved changes.")
    
    # Convert to CSV
    convert_to_csv(tasks)

if __name__ == "__main__":
    main()