class Employee:
    def __init__(self):
        self.name = ""
        self.empId = ""
        self.dept = ""
        self.salary = 0

    def get_emp_details(self):
        self.name = input("Enter Employee name: ")
        self.empId = input("Enter Employee ID: ")
        self.dept = input("Enter Employee Dept: ")
        self.salary = int(input("Enter Employee Salary: "))

    def show_emp_details(self):
        print("Employee Details")
        print("Name: ", self.name)
        print("ID: ", self.empId)
        print("Dept: ", self.dept)
        print("Salary: ", self.salary)

    def update_salary(self):
        self.salary = int(input("Enter new Salary: "))
        print("Updated Salary:", self.salary)

# Create an instance of the Employee class
e1 = Employee()

# Get employee details
e1.get_emp_details()

# Display employee details
e1.show_emp_details()

# Update employee salary
e1.update_salary()
