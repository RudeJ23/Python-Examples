from modAccount import *
from datetime import *

print('calling constructor')
a1 = Account('US Bank', 50,date(2017,1,15))

print('testing getAcctNum')
print(a1.getAcctNum())

print('testing getAcctType')
print(a1.getAcctType())

print('testing getCurrentBalance')
print(a1.getCurrentBalance())

print('testing getBankName')
print(a1.getBankName())

print('testing getOpeningBalance')
print(a1.getOpeningBalance())

print('testing getDateOpened')
print(a1.getDateOpened())

print('')
print('testing str method')
print('')
print(a1)
