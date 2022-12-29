from Employee.Creators.CreatorRegularEmployee import CreatorRegularEmployee
from datetime import time 

def parseScheduleWeek(parseInformation):
    schedules=[]
    fileName = parseInformation.getFileName()
    file = open(fileName,'r')
    for line in file:
        line.rstrip()
        name, schedule = line.split('=')
        days = schedule.split(',')
        employee_schedule = {}
        for day in days:
            startTime, endTime = day.split('-')
            dayOfTheWeek = startTime[0:2]
            startTime,endTime=parseTime(startTime,endTime)
            employee_schedule.setdefault(dayOfTheWeek,(startTime, endTime))
        employee = CreatorRegularEmployee(name,employee_schedule).factory_method()
        
        schedules.append(employee)
    file.close()
    return schedules
                    
def parseTime(startTime,endTime):
    startTime = startTime[2:]
    startTimeHour,startTimeMinute = startTime.split(":")
    endTimeHour,endTimeMinute = endTime.split(":")
    
    startTime = time(int(startTimeHour),int(startTimeMinute))
    endTime = time(int(endTimeHour),int(endTimeMinute))

    return (startTime,endTime)
            

