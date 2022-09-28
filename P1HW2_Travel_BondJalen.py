# Calculating travel expenses 
# 9/21/2022
# CTI-110 P1HW2 - Travel Expense
# Jalen Bond
#

#(psuedo code goes here!)
#Enter a monetary value for budget (budget)
#Enter a string value for travel destination (destn)
#Enter a monetary value for gas (gas)
#Enter a monetary value for travel accomodations (accm)
#Enter a monetary value for food (food)
#Calculate the sum of gas, + food, + accm, to get the monetary value for expenses 
#Calculate the remaining balance by subtracting the monetary value for expenses from the monetary value for budget. 
#Display the string_value for, 'Location'
#Display the string_value for, 'Initial Budget'
#Display the monetary value for, 'Fuel'
#Display the monetary vale for, 'Food'
#Display the monetary value for, 'Remaining Balance'


#Input
print('This program calculates and displays travel expenses')
print()
budget = int(input('Enter budget: > '))
print()
destn = input('Enter your travel destination: > ')
print()
gas = int(input('How much  do you think you will spend on gas?  > '))
print()
accm = int(input('Approximately, how much do you think you will need for accomodation/hotel? > '))
print()
food = int(input('Last, how much do you need for food? > '))
print()

#Process
expenses = gas + accm + food
remaining_balance = budget - expenses

#Output
print('----------Travel Expenses---------')
print('Location: > ', destn)
print('Initial Budget: > ', budget)
print()
print('Fuel: > ', gas)
print('Accomodation: > ', accm)
print('Food: >', food)
print()
print('Remaining Balance: > ', budget - expenses)
hold = input()



