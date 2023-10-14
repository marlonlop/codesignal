"""
After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.
Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

Examples
matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
solution(matrix) = 9.


matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]
the output should be
solution(matrix) = 9

[input] array.array.integer 2d matrix

[output] integer
The total price of all the rooms that are suitable for the CodeBots to live in
"""

def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    cost = 0
    ghostCols = set()    
    
    for row in range(rows):
        for col in range(cols):
            curRoom = matrix[row][col]
            if curRoom != 0 and col not in ghostCols:
                cost += curRoom
            else:
                ghostCols.add(col)
                
    return cost

    
'''
ghostCol = 0, 2, 4, 6, 1
cost = 1 + 2 + 1 + 1 + 5 + 1 + 2 + 3 + 1 

col  0. 1. 2. 3. 4. 5. 6
   [[0, 1, 0, 2, 0, 1, 1], 
    [0, 5, 0, 1, 0, 2, 0], 
    [2, 0, 3, 3, 0, 1, 1]]

'''