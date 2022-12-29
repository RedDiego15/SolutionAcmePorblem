from ParseSchedule.ParseSchedule import ParseSchedule
from ParseSchedule.Strategies.ParseScheduleWeek import parseScheduleWeek, parseTime
from datetime import time


def test_get_schedules():
    parserSchedule = ParseSchedule('file.txt',parseStrategy=parseScheduleWeek)
    schedules = parserSchedule.getSchedules()
    assert len(schedules) ==3


def test_parse_time():
    startTime='MO10:00'
    endTime='12:00'
    newStart,newEnd=parseTime(startTime,endTime)
    assert isinstance(newStart,time)
    assert isinstance(newEnd,time)
