'''
Created on October 14, 2021
@author:   Marguerite Sutedjo
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    else:
        return True
'''base2 representation of 42 = 101010.
With an odd based 10 number the base2 representation last number will be 1
and with and even base 10 number the based 2 last number will be 0.
The original number changes because it would effect the number being even or odd and
would be determined by the second to last number instead of the last number
This would make it easier to find the representation of N because in an even numbered case you could add 1 to the left
of the base 2 number to get Y, if there is an odd numbered case of N the last digit needs to be 1 unless it is already 1'''
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(int(n/2)) + '1'
    else:
        return numToBinary(int(n/2)) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        return binaryToNum(s[:-1]) * 2 + int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return ('0' * 8 + numToBinary(binaryToNum(s) + 1))[-8:]
    '''
    dec = binaryToNum(s)
    b = numToBinary(dec + 1)
    return '0'*max(0, 8 - len(b)) + b[-8:]'''

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0:
        return
    return count(increment(s), n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    #the ternary value for 59 is 2012 because ternary uses 0,1 and 2 instead of binary using 0 and 1
    #continue dividing 59 by 3 and take the remainders of each time you divide it will get the ternary number
    if n == 0:
        return ''
    return numToTernary(int(n / 3)) + str(n % 3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    return ternaryToNum(s[:-1]) * 3 + int(s[-1])
