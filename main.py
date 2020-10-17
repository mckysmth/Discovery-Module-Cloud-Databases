from timeClock import TimeClock

def CreateAccount(tc):
    while tc.emp == None:
        tc.addAccount(input("username: "), input("password: "))
    
    ClockInOut(tc)

def SignIn(tc):
    while tc.emp == None:
        tc.signIn(input("username: "), input("password: "))
    
    ClockInOut(tc)

def ClockInOut(tc):
    while tc.emp != None:
        userInput = input("\n1. Clock In \n2. Clock out\n3. Delete account\n4. Print Report\n5. Sign Out\n" + tc.emp.name + " > " )
        if userInput == "1":
            tc.clockIn()
        elif userInput == "2":
            tc.clockOut()
        elif userInput == "3":
            tc.deletAccount()
        elif userInput == "4":
            tc.printOut()
        elif userInput == "5":
            tc.signOut()
            
        
        else:
            print ("Invalid Command")


def main():
    tc = TimeClock()

    userInput  = None

    while userInput != "quit":
        userInput = input("\n1. Sign In \n2. Create Account\nEnter 'quit' to exit program\n> " )
        if userInput == "1":
            SignIn(tc)
        elif userInput == "2":
            CreateAccount(tc)
        elif userInput != "quit":
            print ("Invalid Command")



if __name__ == "__main__":
    main()