"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example
picture = ["abc",
           "ded"]
the output should be
solution(picture) = ["*****",
                     "*abc*",
                     "*ded*",
                     "*****"]

[input] array.string picture
[output] array.string
"""

def solution(picture):
    rows, cols = len(picture), len(picture[0])
    out = ["*"*(cols + 2)]
    
    for row in range(rows):
        new_row = "*" + picture[row] + "*"
        out.append(new_row)
    out.append("*"*(cols + 2))
    return out