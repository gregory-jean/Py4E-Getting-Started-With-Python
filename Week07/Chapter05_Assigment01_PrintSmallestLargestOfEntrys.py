'''

Assigment 5.2 

Write a program that repeatedly prompts a user 
for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and 
smallest of the numbers. 

If the user enters anything other than a valid 
number catch it with a try/except and put out an 
appropriate message and ignore the number. 

Enter 7, 2, bob, 10, and 4 and match the output below. 

'''

largest = None
smallest = None
finished = False

while finished is False :
    entry = input('Enter a number: ')
    if entry == "done" :
        break
    try :
        entry = int(entry)
    except :
        print("Invalid input")
        continue

    if smallest is None :
        smallest = entry
    if largest is None :
        largest = entry

    if entry < smallest :
        smallest = entry


    if entry > largest :
        largest = entry

print("Maximum is", largest)
print("Minimum is", smallest)