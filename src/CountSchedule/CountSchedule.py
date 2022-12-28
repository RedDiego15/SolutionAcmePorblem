
class CountSchedule():

    def __init__(self,schedule,counting=None):
        self._schedule = schedule
        self._counting = counting
        self._coincidenceCounts={}
        pass
    
    def template_method(self):

        self._coincidenceCounts = self._counting(self._schedule)
        self.formatCoincidence()

    def formatCoincidence(self):
        for (employeeA, employeeB), count in self._coincidenceCounts.items():
            print(f'{employeeA.getName()}-{employeeB.getName()}: {count}')



