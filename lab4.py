#Marguerite Sutedjo
#I pledge my honor that I have abided by the Stevens Honor System.

def knapsack(capacity, itemList):
    '''maximize the value of objects you bring with you, while still being able to carry it'''
    if len(itemList) == 0 or capacity <=0:
        return [0, []]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        lose = knapsack(capacity, itemList[1:])
        use = knapsack(capacity - itemList[0][0], itemList[1:])
        use[0] = itemList[0][1] + use[0]
        use[1] = [itemList[0]]+use[1]
        if use[0] > lose[0]:
            return use
        else:
            return lose
        
    

    
    
