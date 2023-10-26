'''
Created on 10/22/2021
@author:   Richard He, Marguerite Sutedjo
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
## PLEASE READ THE LIMITATIONS WE ENCOUNTERED DURING THIS ASSIGNMENT
'''
So we don't know how to tell the difference if the image starts on a 1 or 0 for compression/decompression
It compresses consecutive sequences that are longer than the 5 bit representation, but it does not alternate between 1 and 0
For example: '1' * 64 with a block size of 5 compresses to '111111111100010', not '11111000001111100000000100'
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

'''
2^4, 2^3, 2^2, 2^1, 2^0 (max 31 pixels of same color in a row)
8x8 image (64 pixels)
'''

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def appendZeros(s):
    '''
    add zeros to the binary represntation so the length of the represenation matches COMPRESSED_BLOCK_SIZE
    '''
    
    if len(s) <= COMPRESSED_BLOCK_SIZE:
        return '0' * (COMPRESSED_BLOCK_SIZE - len(s)) + s
    
def decToBin(x):
    if x == 0:
        return ""
    elif x % 2 == 1:
        return decToBin(x//2) + '1'
    else:
        return decToBin(x//2) + '0'

def binToDec(s):
    if s == '':
        return 0
    else:
        return int(s[-1]) + 2*binToDec(s[:-1])

def countConsec(S, pixelVal, count = 0):
    '''
    counts the number of bits with the same value in a row that can be compressed
    '''
    
    if pixelVal in S[:1] and count < MAX_RUN_LENGTH:
        count += 1
        S = S[1:]
        return countConsec(S, pixelVal, count)
    else:
        return count

def compress(S):
    '''
    compress the image given COMPRESSED_BLOCK_SIZE
    '''
    
    if S == "":
        return ""
    else:
        compressAmount = countConsec(S, S[0])
        # print(compressAmount)
        # print(appendZeros(decToBin(compressAmount)))
        return appendZeros(decToBin(compressAmount)) + compress(S[compressAmount:])

'''
The maximum number of bits compression could produce is 320, which is the worst case checkerboard scenario
Compress would have to allocate 5 bits to represent 1 pixel in a checkerboard image
'''
def uncompress(S):
    '''
    uncompress the image given COMPRESSED_BLOCK_SIZE
    '''
    
    if S == "":
        return ""
    else:
      x ='0' * binToDec(S[:COMPRESSED_BLOCK_SIZE]) + '1' * binToDec(S[COMPRESSED_BLOCK_SIZE:2*COMPRESSED_BLOCK_SIZE])
    return x + uncompress(S[2*COMPRESSED_BLOCK_SIZE:])

def compression(S):
    return len(compress(S)) / len(S)

def testcompress():
    Penguin= "00011000" + "00111100"*3 + "01111110" + "11111111" + "00111100" + "00100100"
    Smile= "0" * 8 + "01100110" * 2 + "0" * 8 + "00001000" + "01000010" + "01111110" + "0" * 8
    Five=  "1" * 9 + "0" * 7 + "10000000" * 2 + "1" * 7 + "0" + "00000001" * 2 + "1" * 7 + "0"
    x = compression(Penguin)
    y = compression(Smile)
    v = compression(Five)
    return x, y, v

'''
The compression ratios we got from Penguin and Smile were both greater than one, which means our compression method was not effective
The compression ratio for Five was still close to one which is not great
We could improve the compression ratios by changing COMPRESSED_BLOCK_SIZE

NASA:
It is impossible to compress an image to a size less than its orignal number of pixels because that would mean COMPRESSED_BLOCK_SIZE would have to be less than 1
This does not make sense
'''

    

     


