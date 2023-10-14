"""
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

For n = 2, the output should be
solution(n) = 5;
For n = 3, the output should be
solution(n) = 13.
Input/Output

[input] integer n

Guaranteed constraints:
1 ≤ n < 104.

[output] integer
The area of the n-interesting polygon.
"""

def solution(n):
    if n == 1:
        return 1
        
    return 2*(n**2) - 2*n + 1
    '''
    n=2                n=3                         n=4

. X .   X X .      . . X . .    X X X . .      . . . X . . .    X X X X . . .
X X X   X X X      . X X X .    X X X X X      . . X X X . .    X X X X X X X
. X .   . . .      X X X X X    X X X X X      . X X X X X .    X X X X X X X
                   . X X X .    . . . . .      X X X X X X X    X X X X X X X
                   . . X . .    . . . . .      . X X X X X .    . . . . . . .
                                               . . X X X . .    . . . . . . .
                                               . . . X . . .    . . . . . . .
    use rectangle to derive formula
    area of rectangle = w * h
    n   height      width   gap
    1   1           1       0
    2   2           3       1
    3   3           5       2
    4   4           7       3    
    n   n           n*n-1   n-1
    formula
        n * (n*2 - 1) - (n-1)
        2n^2 -2n +1
    '''
