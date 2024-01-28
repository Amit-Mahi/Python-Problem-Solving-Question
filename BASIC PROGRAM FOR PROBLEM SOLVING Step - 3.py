# BASIC PROBLEM SOLVING QUESTION FOR PYTHON STEP - 3

# AIM - FIND THE FACTORIAL OF A NUMBER

# QUESTION - 1

# FIND THE FACTORIAL OF A NUMBER USING THE RECURSIVE APPROACH

def factorial(n):

    return 1 if (n==1 or n==0) else n * factorial(n-1)

number = 4

print(factorial(4))


# QUESTION - 2

# FIND THE FACTORIAL OF A NUMBER USING THE ITERATIVE APPROACH (while loop)

def factorial(n):
    if n < 0:
        return 0
    elif n==1 or n==0:
        return 1
    else:
        fact = 1
        while( n > 1):
            fact = fact * n
            n = n - 1

        return fact

number = 4
print(factorial(number))


# QUESTION - 3

# FIND THE FACTORIAL OF A NUMBER USING THE ITERATIVE APPROACH (for loop)

def factorial(n):

    fact = 1

    for i in range(2,n + 1):

        fact = fact * i

    return fact

number = 4
print(factorial(number))


# QUESTION - 4

# FIND THE FACTORIAL OF A NUMBER USING THE IN-BUILT FUNCTION

import math

def factorial(n):

    return(math.factorial(n))

number = 4

print(factorial(number))
      

# QUESTION - 5

# FIND THE FACTORIAL OF A NUMBER USING THE numpy.prod()

import numpy

n = 4

x = numpy.prod([i for i in range(1,n+1)])

print(x)


# QUESTION - 6

#FIND THE FACTORIAL OF A NUMBER USING THE PRIME FACTORIZATION METHOD

def primeFactor(n):
    factors = {}
    i = 2

    while i*i <= n:
        while n%i == 0:
            if i not in factors:
                factors[i] = 0

            factors[i] = factors[i] + 1
            n = n // i
        i = i + 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] = factors[n] + 1
    return factors

def factorial(n):
    result = 1

    for i in range(2,n +1):
        factors = primeFactor(i)

        for p in factors:
            result *= p ** factors[p]

    return result

number = 4
print(factorial(number))
