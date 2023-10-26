'''
Created on October 7th, 2021
@author:   Marguerite Sutedjo
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - HW 4
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1

'''

def pascal_row(n):
    '''takes in a number and outputs a list of elements found in a row of Pascal's triangle'''
    if n < 0:
        return 0
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    else:
        last = pascal_row(n-1)
        new = [1] + pascalRowHelper(last) + [1]
        return new
        
def pascalRowHelper(n):
    '''works through the inside rows and adds the elements in the list'''
    if n == []:
        return []
    elif len(n) == 1:
        return []
    else:
        return [n[0] + n[1]] + pascalRowHelper(n[1:])
    

def pascal_triangle(n):
    '''returns pascal triangle up to n number'''
    if n == 0:
        return [[1]]
    elif n == 1:
        return [[1],[1, 1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    '''tests if pascal_row works'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(2) == [1,2,1]
    assert pascal_row(3) == [1, 3, 3, 1]

def test_pascal_triangle():
    '''tests if pascal_triangle works'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],[1, 5, 10, 10, 5, 1]]
    
