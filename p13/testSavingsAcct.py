from modAccount import *
from datetime import *

print('calling constructor')
a1 = SavingsAcct('US Bank', 50,date(2017,1,15),date(2017,3,10),float(.06))

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

print('testing interest computation')
print(a1.computeInterest(date(2017,2,20)))


print('')
print('testing str method')
print('')
print(a1)

print('testing account close, expecting cannot close')
print(a1.closeAcct(date(2017,3,9)))

print('testing account close, expecting closure')
print(a1.closeAcct(date(2017,3,11)))
