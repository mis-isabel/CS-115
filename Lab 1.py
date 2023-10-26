#Marguerite Sutedjo
#I pledge my honor that I have abided by the Stevens Honor System.
from functools import reduce
from math import factorial
def add(x,y):
    return x + y
def inverse(n):
    """returns the reciprocal of n number"""
    return 1/n
def e(n):
    """returns the approximate value e"""
    list1 = list(range(0, n+1))
    list2 = list(map(factorial, list1))
    list3 = list(map(inverse, list2))
    return reduce(add,list3)
    
