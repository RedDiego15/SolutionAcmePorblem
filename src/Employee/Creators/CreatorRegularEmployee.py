
from Employee.Creators.CreatorEmployee import CreatorEmployee
from Employee.Employees.RegularEmployee import RegularEmployee


class CreatorRegularEmployee(CreatorEmployee):

    
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    def factory_method(self) -> RegularEmployee:
        return RegularEmployee(self.name,self.schedule)