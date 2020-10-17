from datetime import datetime

class PunchIn:

    def __init__(self, clockedInAt = datetime.now(), clockedOutAt = None):
        self.clockedInAt = clockedInAt
        self.clockedOutAt = clockedOutAt

    def punchOut(self, punchOut):
        self.clockedOutAt = datetime.now()