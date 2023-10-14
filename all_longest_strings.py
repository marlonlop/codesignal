"""
Given an array of strings, return another array containing all of its longest strings.

Example
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"]

[input] array.string inputArray
[output] array.string
"""

from collections import defaultdict
def solution(inputArray):
    sMap = defaultdict(list)
    maxLen = 0
    
    for str in inputArray:
        strLen = len(str)
        sMap[strLen].append(str)
        maxLen = max(maxLen, strLen)
        
    return sMap[maxLen]