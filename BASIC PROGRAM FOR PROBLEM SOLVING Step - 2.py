# BASIC PROGRAM FOR PROBLEM SOLVING Step - 2

# AIM - FINDING MAXIMUM NUMBERS IN PYTHON

# QUESTION - 1

# HOW TO FIND THE MAXIMUM USING THE FUNCTION

# INPUT number1 = 2, number2 = 4
# OUTPUT - 4

def maximum(a,b):

    if a >= b:
        return a
    else:
        return b

number1 = 5
number2 = 6

print(maximum(number1, number2))


# QUESTION - 2

# HOW TO FIND THE MAXIMUM USING max()

number1 = 5
number2 = 6

maximum = max(number1, number2)
print(maximum)


# QUESTION - 3

# HOW TO FIND THE MAXIMUM USING TERNARY OPERATOR

number1 = 5
number2 = 6

print(number1 if number1 >= number2 else number2)


# QUESTION - 4

# HOW TO FIND THE MAXIMUM USING LAMBDA FUNCTION

number1 = 5
number2 = 6
max = lambda number1, number2:number1 if number1 > number2 else number2

print(max(number1, number2))


# QUESTION - 5

# HOW TO FIND MAXIMUM NUMBERS USING LIST COMREHENSION

number1 = 5
number2 = 6

x = [number1 if number1 > number2 else number2]

print(x)


# QUESTION - 6

# HOW TO FIND MAXIMUM NUMBERS USING sort() METHOD

number1 = 5
number2 = 6

x = [number1, number2]

x.sort() # this method will brind the maximum number to the last 

print(x[-1])   # -1 index will access the last number of the list ( which was the maximum number from the list)


