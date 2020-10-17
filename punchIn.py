from datetime import datetime

class PunchIn:

    def __init__(self, clockedInAt = datetime.now(), clockedOutAt = None):
        self.clockedInAt = clockedInAt
        self.clockedOutAt = clockedOutAt

    def punchOut(self, punchOut):
        self.clockedOutAt = datetime.now()

    def printLine(self):
        difference = self.clockedInAt - self.clockedOutAt


        print(str(self.clockedInAt) + "\t" + str(self.clockedOutAt))