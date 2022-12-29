import datetime
from CountSchedule.CountingAlgorythms import compareHours

from Employee.Creators.CreatorRegularEmployee import CreatorRegularEmployee

def test_compare_hours():
    reneSchedule = {'MO': (datetime.time(10, 0), datetime.time(12, 0)), 'TU': (datetime.time(10, 0), datetime.time(12, 0)), 'TH': (datetime.time(1, 0), datetime.time(3, 0)), 'SA': (datetime.time(14, 0), datetime.time(18, 0)), 'SU': (datetime.time(20, 0), datetime.time(21, 0))}
    astridSchedule = {'MO': (datetime.time(10, 0), datetime.time(12, 0)), 'TH': (datetime.time(12, 0), datetime.time(14, 0)), 'SU': (datetime.time(20, 0), datetime.time(21, 0))}
    
    employeeA = CreatorRegularEmployee('rene',reneSchedule).factory_method()
    employeeB = CreatorRegularEmployee('astrid',astridSchedule).factory_method()

    assert compareHours(employeeA,employeeB,{(employeeA,employeeB):0}) ==2