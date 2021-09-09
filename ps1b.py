# Name: Riya
# REG. NO.: BS19BTCS005
# Date: 3 Sep,2021
# Time spend: 2:30 hours

#Problem 2
#2.Paying Debt Off In a Year 
"""
Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
We will not be dealing with a minimum monthly payment rate.
"""

outstanding_balance = float(input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))

minimum_monthly_payment  = 500

monthly_interest_rate = annual_interest_rate/12.0

number_of_months = 0

balance = outstanding_balance


#calculate fixed minimum monthly payment

while balance > 0:
    balance = outstanding_balance
    number_of_months = 0
    minimum_monthly_payment  =  minimum_monthly_payment+500
    while balance > 0 and number_of_months < 12:  
        balance = balance * (1 + monthly_interest_rate)- minimum_monthly_payment 
        number_of_months =  number_of_months+1
        
  
print("RESULT")
print("Monthly payment to pay off debt in 1 year: Rs.",float(minimum_monthly_payment))
print("Number of months needed: ",number_of_months)
print("Balance: Rs. ",round(balance,2))
