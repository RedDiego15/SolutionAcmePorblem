from CountSchedule.CountSchedule import CountSchedule
from ParseSchedule.ParseSchedule import ParseSchedule
from ParseSchedule.Strategies.ParseScheduleWeek import parseScheduleWeek
from CountSchedule.CountingAlgorythms import getCoincidenceCountIteration


if __name__ == "__main__":
    
    parserSchedule = ParseSchedule('file.txt',parseStrategy=parseScheduleWeek)
    schedules = parserSchedule.getSchedules()
    countScheduleDict = CountSchedule(schedules,getCoincidenceCountIteration)
    countScheduleDict.template_method() 
    
