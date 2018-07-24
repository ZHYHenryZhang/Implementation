#MIT.PROBLEM SET 2

#1.Paying the Minimum
'''
totalPay=0
Balance=5000
monBalance=Balance
monthlyPaymentRate=0.02
annualInterestRate=0.18

for month in range(0,13):
  MinPayment=monBalance*monthlyPaymentRate
  UnpaidBalance=monBalance-MinPayment
  RemainingBalance=UnpaidBalance*(1+annualInterestRate/12.0)
  print('month:'+str(month))
  print('Minimum monthly payment:'+'%.2f'%MinPayment)
  print('Remaining balance'+'%.2f'%RemainingBalance)
  totalPay=totalPay+MinPayment
  monBalance=RemainingBalance
print('Total Paid:'+'%.2f'%totalPay)
print('Remaining balance:'+'%.2f'%monBalance)

'''

# #2.Paying For the Debt
# balance = 3613
# annualInterestRate = 0.15
# pay=10
# while True:
#     #问题在于这里没有重新设定balance
    
# balance=3613
#     for month in range(12):
#         balance=(balance-pay)*(annualInterestRate/12.0+1)
#     if balance<=0:
#         print('Lowest Payment'+str(pay))
#         break
#     else:
#         pay=pay+10

'''
while True:
    unpaidBalance=balance
    for month in range(12):   #重复12次
        unpaidBalance-=pay
        unpaidBalance=unpaidBalance + unpaidBalance * (annualInterestRate /12.0)
    if unpaidBalance <=0:     #小于或等于零时退出循环
            print('Lowest Payment: '+str(pay))
            break
    else:
        pay+=10
'''

balance = 3613
annualInterestRate = 0.15
for pay in range(10,10000000):
    balance = 3613
    month=0
    while balance>=0:
        balance=(balance-pay)*(annualInterestRate/12.0+1)
        month=month+1
        if month>12:
            break
    else:
        print(10*pay)
        break

        


















