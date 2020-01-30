# simple if statement
'''
x = float(input("enter a number: "))
if (x < 10):
    print('smaller')
if (x > 20):
    print('larger')
print('Finis')
'''

# simple if / else statement
'''
x = float(input("enter a number: "))

if (x > 2) :
    print('bigger')
else :
    print("not bigger")

print('All Done')
'''

# if / else if / else statement
'''
x = float(input("enter a number: "))

if (x < 2) :
    print('small')
elif (x < 10) :
    print("Medium")
else :
    print("LARGE")
print('All done')
'''

# try / except statement

try :
    x = float(input('enter a number'))
except :
    print('invalid input, x set to 25')
    x = 25.0
print('x = ', x)

print('all done')
