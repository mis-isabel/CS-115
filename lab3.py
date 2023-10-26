#Marguerite Sutedjo
#I pledge my honor that I have abided by the Stevens Honor System.

def change(amount, coins):
    '''returns a non-negative integer indicating the minimum number of coins required to make up the given amount'''
    
    if coins == [] and amount > 0 or amount < 0:
        return float("inf")
    elif amount == 0:
        return 0
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        use = 1 + change(amount - coins[0], coins)
        lose = change(amount, coins[1:])
        return min(use, lose)
        

    

    
    
