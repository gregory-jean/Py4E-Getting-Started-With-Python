'''
---------------
Assignment 3.1 
---------------
Write a program to prompt the user for hours 
and rate per hour using input to compute gross pay. 

Pay the hourly rate for the hours up to 40 and 1.5 times 
the hourly rate for all hours worked above 40 hours. 

Use 45 hours and a rate of 10.50 per hour to test the program 
(the pay should be 498.75). 

You should use input to read a string and float() to convert 
the string to a number. Do not worry about error checking the 
user input - assume the user types numbers properly.

'''

shrs = input("Enter Hours:")
ihrs = float(shrs)
othours = 0

# if user worked more than 40 hours, calculate number of overtime hours worked
if(ihrs > 40) :
    othours = ihrs - 40
    ihrs = 40

srate = input("Enter hourly pay:")
irate = float(srate)

# calculate overtime rate
otrate = (irate * 1.5)

# calculate and display pay
pay = ((ihrs * irate) + (othours * otrate))

print(pay)

