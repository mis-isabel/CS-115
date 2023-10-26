'''
Created on October 14th, 2021
@author:   Marguerite Sutedjo
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5 
'''
memo = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    
    if n in memo:
        return memo[n]
    if n < 0:
        return "incorrect input"
    elif n == 0:
        memo[n] = 2
        return 2
    elif n == 1:
        memo[n] = 1
        return 1
    else:
        first_term = fast_lucas(n-1)
        memo[n - 1] = first_term
        second_term = fast_lucas(n-2)
        memo[n - 2] = second_term
        return first_term + second_term

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    elif coins == [] and amount > 0 or amount < 0:
        return float("inf")
    elif coins[0] > amount:
        return fast_change(amount, coins[1:])
    use = fast_change(amount - coins[0], coins)
    lose = fast_change(amount, coins[1:])
    if use + 1 < lose:
        memo[amount] = use + 1
        return use + 1
    else:
        memo[amount] = lose
        return lose
        
      

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


