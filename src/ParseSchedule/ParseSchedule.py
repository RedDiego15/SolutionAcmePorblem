class ParseSchedule:
    
    def __init__(self, fileName, extension,parseStrategy=None):
        self._fileName = fileName
        self._extension = extension
        self._parseStrategy = parseStrategy


    def getSchedules(self):
        schedules={}
        schedules = self._parseStrategy(self) if self._parseStrategy else {'error':'not defined parseStrategy'}
        return schedules

    def getFileName(self):
        return self._fileName

    def getExtension(self):
        return self._extension



