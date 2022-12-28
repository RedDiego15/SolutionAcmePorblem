from Employe.Creators.CreatorRegularEmployee import CreatorRegularEmployee
from ParseSchedule.ParseSchedule import ParseSchedule
from ParseSchedule.Strategies.ParseScheduleWeek import parseScheduleWeek
from datetime import time 


if __name__ == "__main__":
    # print("App: Launched with the ConcreteCreator1.")
    
    # employee = CreatorRegularEmployee('Diego',{}).factory_method()
    # print(employee.getName())
    # print(employee.getSchedule())

    # parserSchedule = ParseSchedule('file.txt',parseStrategy=parseScheduleWeek)
    # schedules = parserSchedule.getSchedules()

    # time1Inicia = time(12,0)
    # time1Fin = time(14,0)
    
    # time2Inicia = time(13,0)
    # time2Fin = time(13,15)
   
    time1Inicia = time(10,15)
    time1Fin = time(12,0)
    
    time2Inicia = time(10,0)
    time2Fin = time(12,0)

    if(time1Inicia<=time2Inicia<=time1Fin and time1Inicia<=time2Fin<=time1Fin ):
        print('funciona')
    
