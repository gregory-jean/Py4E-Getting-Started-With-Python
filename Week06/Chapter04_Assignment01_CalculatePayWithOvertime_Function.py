'''
---------------
Assignment 4.6

Write a program to prompt the user for hours
and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and 
time-and-a-half for the hourly rate for all hours worked above 
40 hours. 

Put the logic to do the computation of pay in a function 
called computepay() and use the function to do the computation. 
The function should return a value. 

Use 45 hours and a rate of 10.50 per hour to test the program 
(the pay should be 498.75). You should use input to read a 
string and float() to convert the string to a number. 
Do not worry about error checking the user input unless 
you want to - you can assume the user types numbers properly. 

Do not name your variable sum or use the sum() function. 
---------------
'''

# Verify and set hours worked
shours = (input("How many hours did you work? "))

try :
    ihours = float(shours)
except :
    print("Invalid entry, please enter a numerical value")
    quit()

# Verify and set hourly wage
swage = (input("What is your hourly wage? "))

try :
    iwage  = float(swage)
except :
    print("Invalid entry, please enter a numerical value")
    quit()

# Calculate pay function
def computepay(hours, wage) :

    otHours = 0
    otWage = 0

    if (hours > 40.0) :
        otHours = (hours - 40)
        otWage = (wage * 1.5)
        hours = 40

    pay = (hours * wage) + (otHours * otWage)
    return pay

# Run function and print pay
paycheckAmount = computepay(ihours, iwage)
print(paycheckAmount)

# Caclulate Gross Pay
def computeGrossPay(hours, wage) :
    otHours = 0
    otWage = 0

    if (hours > 40.0) :
        otHours = (hours - 40)
        otWage = (wage * 1.5)
        hours = 40

    pay = (hours * wage) + (otHours * otWage)
    
    grossPay = (pay * .7)
    return grossPay

grossPaycheckAmount = computeGrossPay(ihours, iwage)
print("Gross Pay:", grossPaycheckAmount)