"""
Given two strings, find the number of common characters between them.

Example
For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

[input] string s1
1 ≤ s1.length < 15
[input] string s2
1 ≤ s2.length < 15

[output] integer
"""


from collections import defaultdict, Counter
def solution(s1, s2):
    commonCount = 0
    #shortMap = defaultdict(int) #not needed here if using Counter()
    
    #determine which string is shorter
    if len(s1) <= len(s2):
        shortStr = s1
        longStr = s2
    else:
        shortStr = s2
        longStr = s1
    
    #build map of shorter str
    # for c in shortStr:
    #     shortMap[c] += 1
    shortMap = Counter(shortStr)
    
    
    #find count of common chars
    for c in longStr:
        if c in shortMap:
            shortMap[c] -= 1
            commonCount += 1
            if shortMap[c] == 0:
                del shortMap[c]
            if commonCount == len(shortStr):
                return commonCount
    
    return commonCount  