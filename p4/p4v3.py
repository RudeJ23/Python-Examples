"""Description: Assignment 4 uses menus and submenus to imitate
a few simple banking functions. Users will initialize their balances, and will
be able to deposit, withdraw, print current balances, print total interest
earned, calculate interest, and close savings.
"""
__author__= "Joe Rude"
__date__= "2/8/2017"

def createMenu(optionList,menuTitle):
    """Description: returns a string that, when printed, will list the options
    vertically with numbers preceding each option
    Precondition: optionList must be a list of strings, menuTitle must
    be a string
    """
    #initialize empty string
    resStr = "" 
    ct = 0
    #print(menuTitle)
    #for-loop iterate over optionList (grabbing one string at a time)
    for eachOption in optionList:
        #increment ct
        ct += 1
        #concatenate the ct onto resStr
        resStr = resStr + str(ct)
        #concatenate the ") " onto resStr
        resStr = resStr + ") "
        #concatenate the element(string) onto resStr
        resStr = resStr + eachOption
        #concatenate the newline character onto resStr \n
        resStr = resStr + "\n"
    return resStr

def getValidChoice(menuString,menuTitle,numOptions):
    """Description: prints the menuTitle and menuString and ask the user to
    enter a choice until they enter a valid numeric choice that is in
    proper range. Returns an integer.
    Preconditions: menuString must be a string that contains the numbered
    options for the choices. menuTitle must be a string. numOptions is an
    integer indicating the number of options for that menu
    """
    #print title, menu options, and ask for user input
    print(menuTitle,"\n")
    print(menuString)
    optionChoice = input("Enter your choice: ")
    digits = '0123456789'
    digitList = list(digits)
    #test for valid user input
    while optionChoice not in digitList or (int(optionChoice) > numOptions)\
            or (int(optionChoice) < 1):
        print("Invalid option choice")
        optionChoice = input("Enter your choice: ")
    optionChoice = int(optionChoice)    
    return optionChoice
            
def processDeposit(balance):
    """Takes the current balance as a parameter. Asks input from user to add
    additional funds to the checking balance. Returns the new balance
    Preconditions: balance is an integer, returns and integer
    """
    amountToAdd = input("Enter amount to add to deposit: ")
    while not amountToAdd.isdigit():
        amountToAdd = input("Invalid number, Enter amount to add to deposit: ")
    amountToAdd = int(amountToAdd)
    balance += amountToAdd
    return balance
    
def processWithdrawl(balance):
    """Takes the current balance as a parameter. Asks input from user to remove
    funds from the checking balance. Returns the new balance.
    Preconditions: balance is an integer, returns an integer. Can't overdraft
    """
    amountToWithdraw = input("Enter amount to withdraw: ")
    while not amountToWithdraw.isdigit() or int(amountToWithdraw) > balance:
        if not amountToWithdraw.isdigit():
            amountToWithdraw = input("Invalid choice. Enter amount to withdraw: ")
        elif int(amountToWithdraw) > balance:
            amountToWithdraw = input("Overdraft not allowed. Enter amount to withdraw: ")
    amountToWithdraw = int(amountToWithdraw)
    
    balance = balance - amountToWithdraw
    return balance

def calculateInterest(interest):
    """Calculates the interest of a given balance at a rate of 1%
    """
    interest = interest * .01
    return interest

def main(): 
    #create menus
    mainMenu = ['Checking','Savings','Print Balances','Exit']
    mainMenuStr = createMenu(mainMenu,"Main Menu:")
    checkingMenu = ['Deposit','Withdraw','Return to Main Menu']
    checkingMenuStr = createMenu(checkingMenu,"Checking Menu:")
    savingsMenu = ['Print Total Interest Earned','Calculate Interest',
                   'Close Savings Account','Return to Main Menu']
    savingsMenuStr = createMenu(savingsMenu,"Savings Menu:")
    
    #user initializes balances
    checking = input("Enter initial checking balance: ")
    while not checking.isdigit():
        checking = input("Invalid number. Enter initial checking balance: ")
    checking = int(checking)
    
    savings = input("Enter initial savings balance: ")
    while not savings.isdigit():
        savings = input("Invalid number. Enter initial savings balance: ")
    savings = int(savings)
    
    #initiate interest rate
    interestRate = .01
    interestTotal = 0
    
    #allow user to navigate menus. call functions when appropriate
    menuChoice = getValidChoice(mainMenuStr,"Main Menu:",4)
    while menuChoice != len(mainMenu):
        #call checking menu
        if menuChoice == 1:
            menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",3)
            while menuChoice != len(checkingMenu):
                if menuChoice == 1:
                    checking = processDeposit(checking)
                    menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",3)      
                if menuChoice == 2:
                    checking = processWithdrawl(checking)
                    menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",3)     
            menuChoice = getValidChoice(mainMenuStr,"Main Menu:",4)
            
        #call savings menu
        if menuChoice == 2:
            menuChoice = getValidChoice(savingsMenuStr,"Savings Menu:",4)
            while menuChoice != len(savingsMenu):
                if menuChoice == 1:
                    print("Total interest earned is ${0:.2f}".format(interestTotal))
                if menuChoice == 2:
                    newInterest = calculateInterest(savings)
                    interestTotal += newInterest
                    savings += newInterest
                    print("Interest earned this period: ${0:.2f}".format(interestTotal))
                if menuChoice == 3:
                    print("Ending Balance: ${0:.2f}.".format(savings),end=" ")
                    print("Savings account closed.",end=" ")
                    print("Total interest earned: ${0:.2f}".format(interestTotal))
                menuChoice = getValidChoice(savingsMenuStr,"Savings Menu:",4)
            menuChoice = getValidChoice(mainMenuStr,"Main Menu:",4)
            
        #print balances
        if menuChoice == 3:
            print("Current checking balance is ${0:.2f}".format(checking))
            print("Current savings balance is ${0:.2f}".format(savings))
            menuChoice = getValidChoice(mainMenuStr,"Main Menu:",4)

    
        
if __name__ == "__main__":
    main()
