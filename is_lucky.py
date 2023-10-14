"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.

Example
For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.

[input] integer n
[output] boolean
"""

def solution(n):
    sum1, sum2 = 0, 0
    nStr = str(n)
    l, r = 0, len(nStr) - 1
    while l < r:
        sum1 += int(nStr[l])
        sum2 += int(nStr[r])
        l += 1
        r -= 1
    
    return sum1 == sum2
    
    '''
    #pythonic solution
    numList = [int(digit) for digit in str(n)]
    mid = len(numList) // 2
    return sum(numList[:mid]) == sum(numList[mid:])
    '''