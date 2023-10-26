#Marguerite Sutedjo
#I pledge my honor that I have abided by the Stevens Honor System.
from cs5png import PNGImage
def mult( c, n ): 
    """ mult uses only a loop and addition  
        to multiply c by the integer n 
    """ 
    result = 0 
    for x in range( n ): 
        result += c
    return result

def update( c, n ): 
    """ update starts with z=0 and runs z = z**2 + c 
         for a total of n times. It returns the final z.  
    """
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

def inMSet(c, n): 
    """ inMSet takes in  
            c for the update step of z = z**2+c 
            n, the maximum number of times to run that step 
        Then, it should return  
            False as soon as abs(z) gets larger than 2 
            True if abs(z) never gets larger than 2 (for n iterations) 
    """ 
    z = 0
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

def scale(pix, pixMax, floatMin, floatMax): 
    """ scale takes in 
            pix, the CURRENT pixel column (or row) 
            pixMax, the total # of pixel columns 
            floatMin, the min floating-point value 
            floatMax, the max floating-point value 
        scale returns the floating-point value that 
            corresponds to pix 
    """
    fromZero = pix / pixMax
    return floatMin + fromZero * (floatMax - floatMin)

def mset(): 
    """ creates a 300x200 image of the Mandelbrot set 
    """ 
    width = 300 
    height = 200 
    image = PNGImage(width, height) 
 
    # create a loop in order to draw some pixels 
     
    for col in range(width): 
        for row in range(height): 
            # here is where you will need 
            # to create the complex number, c!
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y * 1j
            n = 25
            if inMSet( c, n ) == True: 
                image.plotPoint(col, row) 
 
    # we looped through every image pixel; we now write the file 
 
    image.saveFile()
 
