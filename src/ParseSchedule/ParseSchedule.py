class ParseSchedule:
    
    def __init__(self, fileName,parseStrategy=None):
        self._fileName = fileName
        self._parseStrategy = parseStrategy


    def getSchedules(self):
        schedules = self._parseStrategy(self) if self._parseStrategy else ['error not defined parseStrategy']
        return schedules

    def getFileName(self):
        return self._fileName




