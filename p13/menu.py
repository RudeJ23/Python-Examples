from modAccount import *
from datetime import *

def createMenu(titleOfMenu, optionList):
    """Description: returns a string that, when printed, will list the options
    vertically with numbers preceding each option
    Precondition: optionList must be a list of strings
    """
    #print(titleOfMenu)
    #initialize empty string
    resStr = "" 
    ct = 0
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
    options for the choices. menuTitle must be a string. numOptions is a
    positive integer indicating the number of options for that menu
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

def isValidDate(tmp, start, end):
    while not tmp.isdigit() or int(tmp) > end or int(tmp) < start:
        print('Invalid option')
        tmp = input('Enter a valid option: ')
    tmp = int(tmp)
    return tmp

def main():
    
    mainMenu = ['Checking','Savings','Quit']
    mainMenuStr = createMenu("Main Menu:",mainMenu)
    checkingMenu = ['Create a checking account','Print account info', \
                    'Deposit','Withdraw','Print Total Withdrawals',\
                    'Print Total Deposits','Print Current Balance',\
                    'Back to Main']
    checkingMenuStr = createMenu("Checking Menu:",checkingMenu)
    savingsMenu = ['Create a savings account','Close account',
                   'Calculate interest','Print account info',\
                   'Return to Main Menu']
    savingsMenuStr = createMenu("Savings Menu:",savingsMenu)

    menuChoice = getValidChoice(mainMenuStr,"Main Menu:",len(mainMenu))

    countCheckingAccts = 0
    countSavingsAccts = 0
    while menuChoice != len(mainMenu):
        #call checking menu
        if menuChoice == 1:
            menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",len(checkingMenu))
            while menuChoice != len(checkingMenu):
                
                if menuChoice == 1:
                    if countCheckingAccts > 0:
                        return 'Account already created'
                    else:
                        countCheckingAccts += 1
                        userBank = input('Enter bank name: ')
                        userBal = input('Enter opening balance: ')
                        while not userBal.isdigit() or int(userBal) < 0: #check for float
                            print('invalid starting balance')
                            userBal = input('Enter opening balance: ')
                        userBal = float(userBal)
                        userYear = isValidDate(input('Enter a year as ####: '),1,9999)
                        userMonth = isValidDate(input('Enter a month as ##: '),1,12)
                        userDay = isValidDate(input('Enter a date as ##: '),1,31)
                        userDate = date(userYear,userMonth,userDay)
                                               
                        userChecking = CheckingAcct(userBank,userBal,userDate)

                        menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",len(checkingMenu))
                        
                if menuChoice == 2:
                    if countCheckingAccts > 0:
                        print(userChecking)
                    else:
                        print('No account created')
                    menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",len(checkingMenu))

                if menuChoice == 3:
                    if countCheckingAccts > 0:
                        userDeposit = input('Enter amount to deposit: ')
                        while not userDeposit.isdigit() or int(userDeposit) < 0: #check for float
                            print('invalid deposit')
                            userDeposit = input('Enter deposit: ')
                        userDeposit = float(userDeposit)
                        userChecking.deposit(userDeposit)
                    else:
                        print('No account created')
                    menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",len(checkingMenu))
                        
                if menuChoice == 4:
                    if countCheckingAccts > 0:
                        userWithdrawal = input('Enter amount to withdraw: ')
                        while not userWithdrawal.isdigit() or int(userWithdrawal) < 0: #check for float
                            print('invalid starting balance')
                            userWithdrawal = input('Enter opening balance: ')
                        userWithdrawal = float(userWithdrawal)
                        print(userChecking.withdrawal(userWithdrawal))
                    else:
                        print('No account created')
                    menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",len(checkingMenu))

                if menuChoice == 5:
                    if countCheckingAccts > 0:
                        print(userChecking.getTotalWithdrawals())
                    else:
                        print('No account created')
                    menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",len(checkingMenu))

                if menuChoice == 6:
                    if countCheckingAccts > 0:
                        print(userChecking.getTotalDeposits())
                    else:
                        print('No account created')
                    menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",len(checkingMenu))

                if menuChoice == 7:
                    if countCheckingAccts > 0:
                        print(userChecking.getCurrentBalance())
                    else:
                        print('No account created')
                    menuChoice = getValidChoice(checkingMenuStr,"Checking Menu:",len(checkingMenu))

            menuChoice = getValidChoice(mainMenuStr,"Main Menu:",len(mainMenu))
            
        #call savings menu
        if menuChoice == 2:
            menuChoice = getValidChoice(savingsMenuStr,"Savings Menu:",len(savingsMenu))
            while menuChoice != len(savingsMenu):
                if menuChoice == 1:
                    if countSavingsAccts > 0:
                        return 'Account already created'
                    else:
                        countSavingsAccts += 1
                        userBank = input('Enter bank name: ')
                        userBal = input('Enter opening balance: ')
                        while not userBal.isdigit() or int(userBal) < 0: #check for float
                            print('invalid starting balance')
                            userBal = input('Enter opening balance: ')
                        userBal = float(userBal)
                        print('Enter date opened information: ')
                        userYear = isValidDate(input('Enter a year as ####: '),1,9999)
                        userMonth = isValidDate(input('Enter a month as ##: '),1,12)
                        userDay = isValidDate(input('Enter a date as ##: '),1,31)
                        userDate = date(userYear,userMonth,userDay)
                        
                        print('Enter maturity date information: ')
                        userYear = isValidDate(input('Enter a year as ####: '),1,9999)
                        userMonth = isValidDate(input('Enter a month as ##: '),1,12)
                        userDay = isValidDate(input('Enter a date as ##: '),1,31)
                        userMat = date(userYear,userMonth,userDay)
                        
                        userInt = input('Enter interest rate, ex: for 6% interest enter .06: ')
                        #while not userInt.isdigit() or int(userInt) < 0: #check for float
                            #print('invalid interest')
                            #userInt = input('Enter interest rate: ')
                        userInt = float(userInt)
                        
                        userSavings = SavingsAcct(userBank,userBal,userDate,userMat,userInt)

                        menuChoice = getValidChoice(savingsMenuStr,"Savings Menu:",len(savingsMenu))
                        
                if menuChoice == 2:
                    if countSavingsAccts > 0:
                        print('Enter closure date information: ')
                        userYear = isValidDate(input('Enter a year as ####: '),1,9999)
                        userMonth = isValidDate(input('Enter a month as ##: '),1,12)
                        userDay = isValidDate(input('Enter a date as ##: '),1,31)
                        userD = date(userYear,userMonth,userDay)
                        userSavings.closeAcct(userD)
                        countSavingsAccts = 0
                    else:
                        print('No account created')
                    menuChoice = getValidChoice(savingsMenuStr,"Savings Menu:",len(savingsMenu))
                        
                if menuChoice == 3:
                    if countSavingsAccts > 0:
                        print('Enter date information: ')
                        userYear = isValidDate(input('Enter a year as ####: '),1,9999)
                        userMonth = isValidDate(input('Enter a month as ##: '),1,12)
                        userDay = isValidDate(input('Enter a date as ##: '),1,31)
                        userD = date(userYear,userMonth,userDay)
                        userSavings.computeInterest(userD)
                    else:
                        print('No account created')
                    menuChoice = getValidChoice(savingsMenuStr,"Savings Menu:",len(savingsMenu))

                if menuChoice == 4:
                    if countSavingsAccts > 0:
                        print(userSavings)
                    else:
                        print('No account created')
                    menuChoice = getValidChoice(savingsMenuStr,"Savings Menu:",len(savingsMenu))
                        
                #menuChoice = getValidChoice(savingsMenuStr,"Savings Menu:",len(savingsMenu))
            menuChoice = getValidChoice(mainMenuStr,"Main Menu:",len(mainMenu))

if __name__ == '__main__':
    main()
