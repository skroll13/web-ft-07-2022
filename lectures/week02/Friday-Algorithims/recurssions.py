#summation(7)
from math import factorial


# 4*3*2*1
# print(factorial(4))
def factorial(number):
    if number == 1:
        return 1
    number * factorial(number-1)
print(factorial(24))
    
def Power(number, exponent):
    if exponent == 1:
        return number
    else:
        return number * Power(number, exponent - 1)
    
print(Power(5, 3))