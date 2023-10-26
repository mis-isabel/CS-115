#Marguerite Sutedjo
#I pledge my honor that I have abided by the Stevens Honor System.
from functools import reduce
def mult(x, y):
    """Returns the product of x and y"""
    return x * y

def factorial(n):
    """Returns the factorial of n"""
    numbers = list(range(1,n+1))
    return reduce(mult, numbers)

def add(x, y):
    """Returns the sum of x and y"""
    return x + y

def mean(L):
    """Returns the mean of a list"""
    total = reduce(add,L)
    length = len(L)
    return total/length
    
