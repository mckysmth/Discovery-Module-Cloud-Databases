
class Employee:

    def __init__(self, name, password, isClockedIn = False):
        self.name = name
        self.password = password
        self.isClockedIn = isClockedIn


    def clockIn(self):
        self.isClockedIn = True

    def clockOut(self):

        self.isClockedIn = False


