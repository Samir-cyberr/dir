import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w"):
                pass
    
    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        if self.search_employee(employee_id, silent=True):
            print("Error: Employee ID already exists.")
            return
        
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")
        
        print("Employee added successfully!")

    def view_all_employees(self, sorted_by=None):
        try:
            with open(self.FILE_NAME, "r") as file:
                employees = [line.strip() for line in file.readlines()]
                
                if not employees:
                    print("No records found.")
                    return
                
                if sorted_by == "name":
                    employees.sort(key=lambda x: x.split(",")[1])
                elif sorted_by == "salary":
                    employees.sort(key=lambda x: float(x.split(",")[3]))
                
                print("Employee Records:")
                for emp in employees:
                    print(emp)
        except FileNotFoundError:
            print("Error: File not found.")
    
    def search_employee(self, employee_id, silent=False):
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    if line.startswith(employee_id + ","):
                        if not silent:
                            print("Employee Found:")
                            print(line.strip())
                        return line.strip()
        except FileNotFoundError:
            print("Error: File not found.")
        if not silent:
            print("Employee not found.")
        return None
    
    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        records = []
        updated = False
        
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    if line.startswith(employee_id + ","):
                        name = input("Enter new name: ")
                        position = input("Enter new position: ")
                        salary = input("Enter new salary: ")
                        records.append(f"{employee_id},{name},{position},{salary}\n")
                        updated = True
                    else:
                        records.append(line)
            
            if updated:
                with open(self.FILE_NAME, "w") as file:
                    file.writelines(records)
                print("Employee updated successfully!")
            else:
                print("Employee not found.")
        except FileNotFoundError:
            print("Error: File not found.")
    
    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        records = []
        deleted = False
        
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    if line.startswith(employee_id + ","):
                        deleted = True
                    else:
                        records.append(line)
            
            if deleted:
                with open(self.FILE_NAME, "w") as file:
                    file.writelines(records)
                print("Employee deleted successfully!")
            else:
                print("Employee not found.")
        except FileNotFoundError:
            print("Error: File not found.")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                sort_choice = input("Sort by (name/salary/none): ").strip().lower()
                self.view_all_employees(sorted_by=sort_choice if sort_choice in ["name", "salary"] else None)
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
