#Marguerite Sutedjo
#I pledge my honor that I have abided by the Stevens Honor System.

def length(L):
    """Returns the length of the function"""
    x = 0
    for i in L:
        x += 1
    return x

def dot(L, K):
    """Returns the dot product of the lists L and K"""
    le = length(L)
    total = 0
    if (le == 0):
        return 0.0
    elif (le != 0):
        return L[0] * K[0] + dot(L[1:],K[1:])

def explode(S):
    """Takes a string as input and returns a list of characters"""
    if S == '':
        return []
    first = S[:1]
    left = S[1:]
    return [first] + explode(left)

def ind(e, L):
    """find which index in the list has the element e, if not returns length of list"""
    x = 0
    if L == [] or L == '':
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e,L[1:])
    

def removeAll(e, L):
    """removes all mentions of element e from the list"""
    le = length(L)
    if L == []:
        return []
    elif e == L[0]:
        return removeAll(e,L[1:])
    else:
        return  L[:1] + removeAll(e,L[1:])

def myFilter(func, L):
    """Returns if a filtered list"""
    le = length(L)
    if L == []:
        return []
    elif not func(L[0]):
        return myFilter(func,L[1:])
    else:
        return  L[:1] + myFilter(func,L[1:])


##def myFilter(f, l):
##    if l == []:
##        return []
##    elif f(1[0]):
##        return [1[0]] + myFilter(4, l[1:])
##    else:
##        return myFilter(f, l[1:])
##def even(n):
##    return n%2 == 0

def reverse(L):
    """Reverse the elements in a list"""
    newList = L[::-1]
    return newList
def deepReverse(L):
    """reverses all elements in a list including hidden elements"""
    if L == []:
        return L
    elif isinstance(L, (int, float, str)):
        return L
    else:
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    
    
