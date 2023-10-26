# runLenPlus - exercise for fancy version of run length encoding
# D. Naumann, rev 1 Nov 2020, E. Terolli, rev 27 Oct 2021

import math # we need math.log and math.ceil (the ceiling function)

# GOAL: compress/uncompress binary strings using adaptive run-length encoding.

# Builds on a solution for the part of Homework 6, which I refer to 
# as Run Length Encoding (RLE).  If you read carefully and make sure you
# understand each part before going on, you probably won't find this 
# too difficult.  

# Note: we will work with binary strings of characters like '0110', for ease 
# of understanding and testing.  A real-world encoder for a format like 
# zip-files or mp3 files would not use characters!  It would use binary data, 
# where each bit really is one bit, rather than a character code which takes 
# 8 or 16 bits (ASCII or UniCode encoding, respectively).

# The goal is to define functions compressA and uncompressA,
# using run length encoding in an 'adaptive' way.  The possible
# run lengths are based on analysis of the string to be compressed;
# this determines how many bits are used to represent each run length.
# That number must be included in the compressed data, so it can
# be used when un-compressing.

# The compressed format, which I call RLE+, looks like this:
#       bbbwxwxwxwx...
# - bbb is three bits, which represent a number runBits, 0 < runBits < 8
# - each w is a string of runBits bits and encodes the length of a run of 0s
# - each x is a string of runBits bits and encodes the length of a run of 1s
# Note that the wxwxw... part is the same as what is used in Homework 6,
# except in that homework runBits is always 5.

# For example, 010 10 10 01 10  (but without spaces)
#              bbb w  x  w  x
# encodes the string 001101, using runBits=2.

# The compressA function should first scan the input string to determine
# how long is the average run length, avgLen, and then choose a sensible
# number of bits to use for encoding run lengths.  Here is how we will
# choose that number: let runBits be one more than the log of avgLen, 
# but at most 7.  This means we compress using runs of length less 
# than 2**runBits.
# More precisely: 
# let n = math.ceil(math.log(avgLen,2)) + 1 and runBits = min(n,7).

# If runBits is 1, compression is pointless, but we'll do it anyway.

########
# Step 0
# Before working on adaptive RLE, have a look at the code below
# which provides basic RLE.  It's like a solution for Homework 6,
# but the main functions are more general.
########

# Number of bits for data in the Homework 6 RLE format.
# The hw6 assignment refers to this as k, and I refer to it as runBits.
'''
Marguerite Sutedjo
I pledge my honor that I have abided by the Stevens Honor System.
'''

COMPRESSED_BLOCK_SIZE = 5 

MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1 


def numToBinary(n):
    '''String with the binary representation of non-negative integer n,
        with no leading zeros; but empty string if n is 0.'''
    if n==0:
        return ''
    elif n % 2 != 0:
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'

def binaryToNum(s):
    '''Assuming s is a string of 0s and 1s, return the number that s is a
        binary representation of.  For this purpose, the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return 2 * binaryToNum(s[:-1]) + int(s[-1])


def pad(s, runBits) :
    '''Assume 0 <= n < 2**runBits.  Return binary rep of n
        padded with leading 0s to have length runBits.
        For example, numToBinPadded(3, 5) is '00011'. '''
    return '0'*(runBits - len(s)) + s

def count_bit(s, bit):
    """ Assume s is string and bit is the number 0 or 1 (not character!).
        Return the number of times the bit is observed until reaching the inverted bit.
        For example, if s = "00111" and bit = 0 it will return 2"""
    bit = str(bit)
    if s == "":
        return 0
    if s[0] == bit:
        return 1 + count_bit(s[1:], bit)
    else:
        return 0
    
def compressX(s, b, runBits):
    '''Assume s is string and b is the number 0 or 1 (not character!).  
        Return RLE of s starting with the num of b's at start of s (which 
        may be none).  Each run length is encoded using exactly runBits bits.'''
    if s=='':
        return ''
    else:
        maxRunLen = 2**runBits - 1
        bits = count_bit(s[:maxRunLen], b)
        return pad(numToBinary(bits), runBits) + compressX(s[bits:], 1 - b, runBits)

def compress(s):
    '''Return the RLE of s using COMPRESSED_BLOCK_SIZE-bit run lengths.'''
    return compressX(s, 0, COMPRESSED_BLOCK_SIZE)

def uncompressX(s, b, runBits):
    '''Assume s is in wxwx... or xwxw... format, depending on whether
    b is 0 or 1. Return the string that s encodes.'''
    if s=='': return ''
    else:
        n = binaryToNum(s[:runBits])
        return n*str(b) + uncompressX(s[runBits:], 1-b, runBits)

def uncompress(s):
    '''Return the string that s encodes, assuming RLE with COMPRESSED_BLOCK_SIZE-bit run lengths.'''
    return uncompressX(s, 0, COMPRESSED_BLOCK_SIZE)

########
# Step 1
# Complete the following definition.
# The helper lORL should be tail recursive, and use the accumulator technique.
########

L0 = '1110001111001010' # runBits will be 2
L1 = '1'                # runBits will be 1
L2 = '111111110101010101010101010101010101010101' # runBits 2
L3 = '110011001100'     # runBits 2
L4 = '000111000111'     # runBits 3 (is this ideal?)
L5 = '0000111100001111' # runBits 3
# The following three are from test_hw6.py and have runBits 6
L6 = '0' * MAX_RUN_LENGTH + '1' * MAX_RUN_LENGTH + '0' * (64 - 2 * MAX_RUN_LENGTH)
L7 = '0' * (MAX_RUN_LENGTH + 1) + '1' * (MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * MAX_RUN_LENGTH - 2)
L8 = '1' * MAX_RUN_LENGTH + '0' * MAX_RUN_LENGTH + '1' * (64 - 2 * MAX_RUN_LENGTH)


def listOfRunLengths(s):
    '''Assume s is a nonempty string.  Return a list of the lengths of its runs.
        For the list L0 above, listOfRunLengths(L0) is [3,3,4,2,1,1,1,1].'''

    def lORL(s, result, curCount, curVal):
        '''Accumulate, in result, the list of run lengths of s, using
            curCount as count of the current run; the current run 
            is a sequence of curVals.'''

        if s == '':
            return result + [curCount]
        elif s[0] == curVal:
            return lORL(s[1:], result, curCount + 1, curVal)
        else:
            return lORL(s[1:], result + [curCount], 1, s[0])
##        if len(s) == 1:
##            if s[0] == curVal:
##                curCount += 1
##            else:
##                curCount = 1
##            result = result + [curCount]
##            return result
##        elif s[0] == curVal and curCount < MAX_RUN_LENGTH:
##            curCount += 1
##            return lORL(s[1:], result, curCount, curVal)
##        else:
##            result = result + [curCount]
##            curCount = 1
##            curVal = s[0]
##            return lORL(s[1:], result, curCount, curVal)
        
            
    return lORL(s[1:], [], 1, s[0]) # don't change this line
    # first run begins with s[0] and has length 1 so far


########
# Step 2
# Complete the following definition.
########

def findRunBits(s):
    '''Returns the number of bits to use for compressing string s.
        Assume s is a nonempty string.
        Specifically, returns n where n is the log of the average
        run length, but at most 7, as described at the beginning of this file.
        The maximum n is 7 because only three bits are available
        for it (the bbb in the compressed format).'''
    runLength = listOfRunLengths(s)
    average = sum(runLength) / len(runLength)
    n = math.log(average, 2)
    if n <= 7:
        return math.ceil(n) + 1
    else:
        return 7
    # My solution is four lines of code, no recursion, but using the
    # built-in sum, min, and len functions as well as log and ceiling.

########
# Step 3 
# Here are compressA and uncompressA using the preceding functions.
# Check your work by testing these functions. One way to test is
# check whether uncompressA(compressA(s)) == s, for various s including
# the strings L0, L1, ... in this file.
#
# This is for your benefit.  Step 3 is not graded.
########

def compressA(s):
    '''Returns compressed form of s using RLE+ format.'''
    runBits = findRunBits(s) # expect 0 < runBits < 8
    bbb = pad(numToBinary(runBits), 3)
    return bbb + compressX(s, 0, runBits)

def uncompressA(s):
    '''Assume s is a string of 0s and 1s in the RLE+ format above.
    Return the string that it encodes.'''
    bbb = s[0:3]                # get runBits
    runBits = binaryToNum(bbb)  # convert it to an integer
    wxs = s[3:]                 # the encoded data 
    return uncompressX(wxs, 0, runBits)


########
# EXTRA CHALLENGE (not for a grade, just for practice)
# In some cases, the compressed version will actually be longer than the original.
# Here's a way to avoid it ever being more than one bit longer.
#
# The idea is to change the file format so it looks like this:
#       y.....
# where y is 0 or 1.  If y is 0 it means no compression was done, and the rest 
# of the string is the original.  For example, 01010 represents the string 1010.
# If y is 1 it means the rest of the string is encoded using RLE+.  In that case
# we can write the encoded string as 1bbbwxwxwxwx... where bbbwxwxwx... is RLE+
# format.  
# 
# To decode a string s, check the first bit i.e. s[0].  If it's 0, then the 
# original string is s[1:].  Otherwise, s[0] should be 1 and we can decode
# it by uncompressA(s[1:]).  
#
# To encode a string s, first set t = compressA(s).  If len(t)>len(s) then 
# just put 0 in front of s.  Otherwise, put 1 in front of t.  
#



