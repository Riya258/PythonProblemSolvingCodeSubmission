
# Name: Riya
# REG.NO.: BS19BTCS005
# Date: 30 August,2021
# Time spend:35 min

# Problem Set #1
#Problem 1
""" Write a program to calculate the credit card balance after one year if a person only pays the
    minimum monthly payment required by the credit card company each month. """

outstanding_balance = int(input("Enter the outstanding balance on your credit card: "))

ann_interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))

min_mon_pay_rate = float(input("Enter the minimum monthly payment rate as a decimal: "))


total_months = 12
total_amount = 0
for i in range (0,12):
    print("month ",i+1)
   
    minimum_monthly_payment = min_mon_pay_rate * outstanding_balance
    
    interest_paid = ann_interest_rate/total_months*outstanding_balance
    
    principal_paid = minimum_monthly_payment - interest_paid
    
    remaining_balance = outstanding_balance - principal_paid
    outstanding_balance = remaining_balance
    total_amount += minimum_monthly_payment
    print("Minimum monthly payment: Rs.",round(minimum_monthly_payment,2))
    print("Principal Paid: Rs.",round(principal_paid,2))
    print("Remaining balance: Rs.",round(remaining_balance,2))

print("RESULT")
print("Total amount paid: Rs.",format(total_amount,".2f"))
print("Remaining balance: Rs.",format(remaining_balance,".2f"))