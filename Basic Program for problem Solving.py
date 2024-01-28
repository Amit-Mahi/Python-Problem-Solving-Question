# WELCOME TO PYTHON BASIC PROGRAMS
# AIM - PROOBLEM SOLVING QUESTION

# QUESTION -1

# HOW TO ADD NUMBERS IN PYTHON

# INPUT - number1 = 8, number2 = 7
# OUPUT - 15

number1 = 8
number2 = 7
sum = number1 + number2
print(sum)


# QUESTION - 2

# HOW TO SUBTRACT NUMBERS WITH USER INPUT

number1 = input("Enter your First Number : ")
number2 = input("Enter your Second Number : ")
sub = int(number1) - int(number2)  # we have to convert the user input into integers ( bcz by default its string)
print(sub)


# QUESTION - 3

# HOW TO MULTIPLY NUMBERS USING FUNCTION

def multi(a,b):  # define the function first
    return a*b    # return statment execute the operation

print(multi(2,3))  # calling the function and giving the values to the argunments define in the function and printing it at the same time.


# QUESTION - 4

# HOW TO ADD NUMBERS USING OPERATORS

number1 = 15
number2 = 5

import operator
addition = operator.add(number1, number2)

print(addition)

# QUESTION - 5

# HOW TO ADD NUMBERS USING LAMBDA FUNCTION

number1 = 5
number2 = 6

addition = lambda x,y: x+y  #defining the lambda function

sum = addition(number1,number2) # call the function and store in a variable
print(sum)

# QUESTION - 6

# HOW TO ADD NUMBERS USING RECURSIVE FUNCTION

def addition(x,y):
    if y == 0:
        return x
    else:
        return addition(x+1,y-1)  # the recursive funtion break when y = 0 until it will call it self

number1 = 4
number2 = 5

sum = addition(number1, number2)
print(sum)

