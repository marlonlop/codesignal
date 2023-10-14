"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190]

[input] array.integer a
If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

[output] array.integer
Sorted array a with all the trees untouched
"""

def solution(a):
    sorted_heights = sorted([height for height in a if height != -1])
    person_index = 0
    
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sorted_heights[person_index]
            person_index += 1
    return a