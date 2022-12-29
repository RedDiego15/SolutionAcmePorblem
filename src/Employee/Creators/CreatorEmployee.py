from abc import ABC, abstractmethod

from Employee.Employees.Employee import Employee


class CreatorEmployee(ABC):

    @abstractmethod
    def factory_method(self)->Employee:
        pass


    