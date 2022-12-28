
import datetime
def getCoincidenceCountIteration(schedule):
    coincidences={}
    for i in range(len(schedule)):
        for j in range(i+1,len(schedule)):

            employeeA = schedule[i]
            employeeB = schedule[j]
            coincidences[(employeeA,employeeB)]=0
            compareHours(employeeA,employeeB,coincidences)
    return coincidences

            
def compareHours(employeeA,employeeB,coincidences):
    scheduleEmployeeA = employeeA.getSchedule()
    scheduleEmployeeB = employeeB.getSchedule()

    for day in scheduleEmployeeA.keys():
        if(day in scheduleEmployeeB.keys()):
            timeAstart = scheduleEmployeeA[day][0]
            timeAfin = scheduleEmployeeA[day][1]
            
            timeBstart = scheduleEmployeeB[day][0]
            timeBfin = scheduleEmployeeB[day][1]
            if((timeAstart<=timeBstart<=timeAfin and timeAstart<=timeBfin<=timeAfin) or
                (timeBstart<=timeAstart<=timeBfin and timeBstart<=timeAfin<=timeBfin) ):
                    coincidences[(employeeA,employeeB)] += 1
