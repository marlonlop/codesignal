"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.
Input strings will always be well-formed with matching ()s.

Example
For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim"

[input] string inputString
[output] string
"""
def solution(inputString):
    stack = []
    
    for char in inputString:
        if char == ")":
            reversedStr = ""
            while stack[-1] != "(":
                reversedStr += stack.pop()
            stack.pop() # pop the (
            for c in reversedStr:
                stack.append(c)
        else:
            stack.append(char)
    
    return "".join(stack)
