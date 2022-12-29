from Employee.Employees.Employee import Employee

class RegularEmployee(Employee):
    
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule


    def getName(self) -> str:
        return self.name

    def getSchedule(self) -> str:
        return self.schedule
