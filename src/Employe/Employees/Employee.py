from abc import ABC, abstractmethod

class Employee(ABC):



    @abstractmethod
    def getName(self) -> str:
        pass
    
    @abstractmethod
    def getSchedule(self) -> str:
        pass
