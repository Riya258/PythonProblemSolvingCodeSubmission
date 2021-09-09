# Name: Riya
# Reg. No.: BS19BTCS005
# Time spend: 2:30 hours

#Problem 3
"""
Write a program that uses these bounds and bisection search to find the smallest monthly payment
to the paisa (no more multiples of Rs.500) such that we can pay off the debt within a year.
"""

outstanding_balance = float(input("Enter the outstanding balance on your credit card: "))

ann_interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))

number_of_months = 0

elipson = 0.01 

balance = outstanding_balance

monthly_interest_rate = ann_interest_rate/12.0

balance = outstanding_balance

monthly_payment_lower_bound = balance / 12.0

monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate) * 12.0) / 12.0


while abs(balance) > elipson:
    minimum_monthly_payment = (monthly_payment_upper_bound + monthly_payment_lower_bound)/2
    balance = outstanding_balance
    number_of_months = 0
    while number_of_months < 12:
        balance = balance * (1 + monthly_interest_rate)- minimum_monthly_payment 
        number_of_months =   number_of_months+1
    if balance > elipson:
        monthly_payment_lower_bound = minimum_monthly_payment
    elif balance < elipson:
        monthly_payment_upper_bound = minimum_monthly_payment
    else:
        break 
      

print("RESULT")
print("Monthly payment to pay off debt in 1 year: Rs.",format(minimum_monthly_payment,".2f"))
print("Number of months needed: ",number_of_months)
print("Balance: Rs.",format(balance,".2f"))
