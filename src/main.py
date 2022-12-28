from Employe.Creators.CreatorRegularEmployee import CreatorRegularEmployee
from ParseSchedule.ParseSchedule import ParseSchedule
from ParseSchedule.Strategies.ParseScheduleWeek import parseScheduleWeek


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    
    employee = CreatorRegularEmployee('Diego',{}).factory_method()
    print(employee.getName())
    print(employee.getSchedule())

    parserSchedule = ParseSchedule('file','.txt',parseStrategy=parseScheduleWeek)
    parserSchedule.getSchedules()


