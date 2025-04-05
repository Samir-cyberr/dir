try:
    with open('example.txt', "w+") as file:
        file_handler = open('example.txt')
        Employee_ID = input(" Write Employee ID :")
        Name = input(" Write employee name:")
        Position = input(" Write employer position:")
        Salary = input(" Write employer salary :")
        """def write( Employee_ID1: str,
                Name1 : str,
                Position1: str
                ):"""
        file_handler.write(Employee_ID)
        file_handler.write(Name)
        file_handler.write(Position)
        file_handler.write(Salary)
        file_handler.read('example.txt') 
        file_handler.close()
           #return write
except:
    print("mm")
pass