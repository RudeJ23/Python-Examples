"""Description: Program 13 uses Inheritance to create the parent class Account
and the child classes CheckingAcct and SavingsAcct. It's tested with the
included files.
"""
__author__= "Joe Rude"
__date__= "4/19/2017"

class Account:
    _lastAcctNumUsed = 100

    def __init__(self, tmpBankName, tmpOpenBal, dateOpened):
        '''Description: constructor for creating a general account
           Precondition: tmpBankName is a string, tmpOpenBal is a float greater
           or equal to zero, and dateOpened is a date type'''
        self._acctNum = Account._lastAcctNumUsed
        Account._lastAcctNumUsed += 1
        self._bankName = tmpBankName
        self._acctType = 'general'
        self._openingBalance = float(tmpOpenBal)
        self._currentBalance = float(tmpOpenBal)
        self._dateOpened = dateOpened

    def getAcctNum(self):
        '''Description: gets and returns the account number for an Account obj
           Precondition: self is an Account obj
        '''
        return self._acctNum

    def getAcctType(self):
        '''Description: gets and returns the account type for an Account obj
           Precondition: self is an Account obj
        '''
        return self._acctType

    def getCurrentBalance(self):
        '''Description: gets and returns the current balance of the account
           Precondition: self is an Account obj
        '''
        return self._currentBalance

    def getBankName(self):
        '''Description: gets and returns the bank name of the account
           Precondition: self is an Account obj
        '''
        return self._bankName

    def getOpeningBalance(self):
        '''Description: gets and returns the opening balance of an account
           Precondition: self is an Account obj
        '''
        return self._openingBalance

    def getDateOpened(self):
        '''Description: gets and returns the date the account was opened
           Precondition: self is an Account obj
        '''
        return self._dateOpened

    def __str__(self):
        '''Description: returns a string containing the information for
        the account, labeling each item
        '''
        tmp = ''
        tmp += 'Account Num: ' + str(self._acctNum) + '\n'
        tmp += 'Account Type: ' + str(self._acctType)+ '\n'
        tmp += 'Opening Balance: $' + \
               str('{:4.2f}'.format(float(self._openingBalance))) +'\n'
        tmp += 'Current Balance: $' + \
               str('{:4.2f}'.format(float(self._currentBalance))) +'\n'
        tmp += 'Bank Name: ' + str(self._bankName)+ '\n'
        tmp += 'Date Opened: ' + (self._dateOpened).strftime('%m/%d/%y') +'\n'
        return tmp

class CheckingAcct(Account):

    def __init__(self,tmpBankName,tmpOpenBal,dateOpened):
        '''Description: child class constructor for a CheckingAcct type of the
           parent class Account
           Precondition: tmpBankName is a string, tmpOpenBal is a float greater
           or equal to zero, and dateOpened is a date type
        '''
        Account.__init__(self,tmpBankName,tmpOpenBal,dateOpened)
        self._acctType = 'checking'
        self._currentBalance = float(tmpOpenBal)
        self._totalDeposits = float(0)
        self._totalWithdrawals = float(0)

    def deposit(self, amt):
        '''Description: allows for the user to deposit an amount into a checking
           account
           Precondition: amt is a float greater or equal to zero
        '''
        self._totalDeposits += amt
        self._currentBalance += amt

    def withdrawal(self, amt):
        '''Description: allows for the user to withdraw from the checking
           account.
           Precondition: amt is a float, not allowed to overdraft
        '''
        if amt > self._currentBalance:
            return 'Overdrafts not allowed'
        else:
            self._totalWithdrawals += amt
            self._currentBalance -= amt
            return 'Successfull withdrawal'

    def getTotalWithdrawals(self):
        '''Description: returns the total amount of withdrawals made to an
           account.
           Precondition: self is an Account type object
        '''
        return self._totalWithdrawals

    def getTotalDeposits(self):
        '''Description: returns the total deposits made to an account
           Precondition: self is an Account type object
        '''
        return self._totalDeposits
    
    def __str__(self):
        '''Description: adds additional information and labels to the output
           of the parent Account class related to checking accounts.
           Precondition: None
        '''
        tmp = Account.__str__(self)
        tmp += 'Total deposits: $' + \
               str('{:4.2f}'.format(float(self._totalDeposits))) +'\n'
        tmp += 'Total withdrawals: $' + \
               str('{:4.2f}'.format(float(self._totalWithdrawals)))
        return tmp

class SavingsAcct(Account):

    def __init__(self,tmpBankName,tmpOpenBal,dateOpened,maturityDate,intRate):
        '''Description: child constructor for the parent Account class
           Precondition: tmpBankName is a string, tmpOpenBal is a float greater
           than or equal to zero, dateOpened and maturityDate are date types,
           and intRate is a float type.
        '''

        self._maturityDate = maturityDate
        self._interestRate = float(intRate)
        self._lastDateInterestAdded = dateOpened
        Account.__init__(self,tmpBankName,tmpOpenBal,dateOpened)
        #self._currentBalance = float(tmpOpenBal)
        self._acctType = 'savings'
        self._totalInterestEarned = float(0)

    def computeInterest(self, tmpDate):
        '''Description: if 30 days have passed since the lastDateInterestAdded,
           multiply the currentBalance by the interest rate. After, the
           currentBalance, totalInterestEarned, and lastDateInterestAdded
           are updated
           Precondition: self is an Account obj and tmpDate is a date type
        '''
        if (tmpDate - self._lastDateInterestAdded).days >= 30:
            tmpNum = self._currentBalance * self._interestRate
            self._currentBalance += tmpNum
            self._totalInterestEarned += tmpNum
            self._lastDateInterestAdded = tmpDate
            return 'interest computed'
        else:
            return '30 days have not passed'

    def __str__(self):
        '''Description: Adds additional labels and output to the string method
           from the parent Account class that relates to savings accounts.
           Precondition: None
        '''
        tmp = Account.__str__(self)
        tmp += 'Maturity date: ' + (self._maturityDate).strftime('%m/%d/%y') +'\n'
        tmp += 'Interest Rate: $' + \
               str('{:4.2f}'.format(float(self._interestRate))) +'\n'
        tmp += 'Total interest earned: $' + \
               str('{:4.2f}'.format(float(self._totalInterestEarned))) +'\n'
        tmp += 'Last date interested was added: ' + \
               (self._lastDateInterestAdded).strftime('%m/%d/%y') +'\n'
        return tmp

    def closeAcct(self, d):
        '''Description: Closes a savings account if d is greater than the
           maturity date. If d is earlier, returns a string 'Cannot close'
           If d is later than the maturityDate, returns 'Successfully closed'
           Precondition: self is an Account obj and d is a date type
        '''
        if d < self._maturityDate:
            return 'Cannot close'
        else:
            return 'Successfully closed'

        
    






    
        
