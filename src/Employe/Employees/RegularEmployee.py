from abc import ABC, abstractmethod

class RegularEmployee(ABC):
    
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule


    def getName(self) -> str:
        return self.name

    def getSchedule(self) -> str:
        return self.schedule
