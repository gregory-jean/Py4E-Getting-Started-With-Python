# Loops
'''
for i in [5, 4, 3, 2, 1] :
    print(i)
'''

# Video 5.3 Notes
'''
print('Before')
for thing in [9, 41, 12, 3, 74, 15] :
    print(thing)
print("After")
'''

# What is the largest number?

'''
Think how would the computer approach the problem
'''

'''
largest_so_sar = -1
print("Before", largest_so_sar)

for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_sar :
        largest_so_sar = the_num
    print(largest_so_sar, the_num)

print('After', largest_so_sar)

'''

# Video 5.4 Notes


# Counting in a loop
'''
To count how many times we execute a loop, 
we introduce a counter variable that starts 
at 0 and we add one to it each time through the loop.

'''
'''
count = 0
print("Before", count)
for thing in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    print(count, thing)
print("After", count)
'''


# Total of a loop

'''
To add up a value we encounter in a loop, 
we introduce a sum variable that starts at 0
and we add the value to the sum each time through the loop.

'''
'''
total = 0
print("Before", total)
for thing in [9, 41, 12, 3, 74, 15] :
    total = total + thing
    print(total, thing)
print("After", total)

'''

# Finding the Average

'''
An average just combines the counting and sum patterns
and divides when the loop is done
'''
'''
count = 0
sum = 0

print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value   
    print(count, sum)
print("After", count, sum, (sum / count))
'''

# Filtering in a loop

'''
We use an if statement in the loop to catch / filter 
the values we are looking for.
'''
'''
print("Before")
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20:
        print('Large Number', value)
print("After")
'''

# Search Using a Boolean Variable

'''
If we just want to search and know if a value was found,
we use a variable that starts at False and is set to True
as soon as we find what we are looking for.
'''
'''
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print('After', found)
'''

# How to find the smallest value

'''
'''

smallest_so_far = None
print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if smallest_so_far is None :
        smallest_so_far = the_num
    elif the_num < smallest_so_far :
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After', smallest_so_far)