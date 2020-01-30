'''
---------------
Assignment 3.3
---------------
Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, print a grade 
using the following table:

Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F

If the user enters a value out of range, 
print a suitable error message and exit. 
For the test, enter a score of 0.85. 

'''
# Take in score and parse for an int
sscore = input("Enter and score between 0.0 and 1.0. The output will display associated the letter grade : ")
try :
    iscore = float(sscore)
except:
    print("Error, please enter a numeric value")
    quit()

# Determine letter grade to display
if (iscore > 1.0) :
    print('Entered value out of range. Please enter a value between 0.0 and 1.0')
elif(iscore >= 0.9) :
    print('A')
elif (iscore >= 0.8) :
    print('B')
elif (iscore >= 0.7) :
    print('C')
elif (iscore >= 0.6) :
    print('D')
elif (iscore < 0.6) :
    print('F')
else :
    print('Entered value out of range. Please enter a value between 0.0 and 1.0')




'''
Initial attempt before watching the assignment help video. 
Submitted to Coursera for assignment, passing grade.

try :
    score = float(input('Enter and score between 0.0 and 1.0. The output will display associated the letter grade : '))
    if (score > 1.0) :
        print('Entered value out of range')
    elif(score >= 1.0) :
        print('A')
    elif (score >= 0.8) :
        print('B')
    elif (score >= 0.7) :
        print('C')
    elif (score >= 0.6) :
        print('D')
    elif (score < 0.6) :
        print('F')
    else :
        print('Entered value out of range')
except:
    print('Invalid entry, exiting program.')

'''