# nim template DNaumann (2018), for assignment nim_hw11.txt 
#Marguerite Sutedjo
#I pledge my honor that I have abided by the Stevens Honor System.


# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print("Congratulations you won the game!")

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            print("Unfortunately the computer won and you lost :(")

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    
    while True:
        num_piles = int(input("Number of piles? "))
        if num_piles > 0:
            break
        else:
            print("Invalid input, please try again")
    piles = [0]*num_piles
    for x in range(num_piles):
        while True:
            pileAmount = int(input("Number of coins in pile " + str(x + 1) + "? "))
            if pileAmount > 0:
                piles[x] = pileAmount
                break
            else:
                print("Invalid input, please try again")
        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    for x in range(num_piles):
        print("Pile " + str(x + 1) + " = " + str(piles[x]))


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    while True:
        pileNum = int(input("Choose Pile Number. "))
        if pileNum <= num_piles and pileNum > 0:
            if piles[pileNum - 1] <= 0:
                print("Pile " + str(pileNum) + "is empty, try again. ")
            else:
                break
        else:
            print("Pile doesn't exist, try again. ")
    return pileNum - 1


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    print("Pile " + str(pnum + 1) + " has " + str(piles[pnum]) + " coin(s). ")
    while True:
        minus = int(input("Amount of coins to remove? "))
        if minus <= piles[pnum] and minus > 0:
            break
        else:
            print("Invalid input, try again. ")
    return minus
            


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 

    nim = 0
    for x in piles:
        nim = nim ^ 1
    return nim


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles
    
    gNim = game_nim_sum()
    pNim = [0]*num_piles
    
    for x in range(num_piles):
        pNim[x] = piles[x] ^ gNim
        if pNim[x] < piles[x] and piles[x] != 0:
            human = piles[x] - pNim[x]
            return x, human
    for x in range(num_piles):
        if piles[x] != 0:
            return x, 1

def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    computer = opt_play()
    piles[computer[0]] -= computer[1]
    print("I remove " + str(computer[1]) + " coin(s) from pile " + str(computer[0] + 1))

    


#   start playing automatically
if __name__ == "__main__" : play_nim()
