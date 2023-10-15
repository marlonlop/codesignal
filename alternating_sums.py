"""
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.
You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

Example
For a = [50, 60, 60, 45, 70], the output should be
solution(a) = [180, 105].

[input] array.integer a
[output] array.integer
"""

def solution(a):
    out = [0]*2
    t1, t2 = 0, 1
    aLen = len(a)
    
    while t1 < aLen or t2 < aLen:
        out[0] += a[t1] if t1 < aLen else 0
        out[1] += a[t2] if t2 < aLen else 0
        # upd indices
        t1 += 2
        t2 += 2
    
    return out