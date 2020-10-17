from googleFireBase import GoogleFireBase
from employee import Employee
from punchIn import PunchIn

import datetime

class TimeClock:

    def __init__(self):
        self.db = GoogleFireBase.initialize_firestore()
        self.emp = None
        
    def addAccount(self, eName, ePassword):
        self.emp = Employee(eName, ePassword)
        if GoogleFireBase.find_player(self.db, self.emp) == None:
            GoogleFireBase.set_employee(self.db, self.emp)
        else:
            self.emp = None
            print("Username already exists.\n")

    def signIn(self, eName, ePassword):
        self.emp = Employee(eName, ePassword)
        tempEmp = GoogleFireBase.find_player(self.db, self.emp)
        tempEmp = Employee(tempEmp["name"], tempEmp["password"],  tempEmp["isClockedIn"])
        if tempEmp != None:
            if tempEmp.password == ePassword:
                self.emp = tempEmp
            else:
                self.emp = None
                print("Incorrect/Password username.\n")

        else:
            self.emp = None
            print("Incorrect/Password username.\n")

    
    def signOut(self):
        self.emp = None

    
    def clockIn(self):
        if not self.emp.isClockedIn:
            self.emp.clockIn()
            GoogleFireBase.set_punchIn(self.db, PunchIn(), self.emp)
            
            GoogleFireBase.set_employee(self.db, self.emp)
        else:
            print ("\nYou are already clocked in.\n")

    def clockOut(self):
        if self.emp.isClockedIn:
            self.emp.clockOut()
            GoogleFireBase.get_last_punchIn(self.db,self.emp)
            GoogleFireBase.set_employee(self.db, self.emp)
        else:
            print ("\nYou are not clocked in.\n")

    def deletAccount(self):
        userInput = input("Are you sure you want to delete the account? [y/n] > " )

        if userInput == "y":
            GoogleFireBase.delet_account(self.db, self.emp)
            print ("\nAccount successfully deleted.\n")
            print ("\nSigning Out.\n")
            self.emp = None

    def printOut(self):
        docs = GoogleFireBase.get_all_PIO(self.db, self.emp)

        print("CLOCK IN\t\t\t\t CLOCK OUT\t\t\t\t")
        for doc in docs:
            pio_dict = doc.to_dict()
            poi = PunchIn(pio_dict["clockedInAt"], pio_dict["clockedOutAt"])
            poi.printLine()