# LC74.Search_a_2D_Matrix.py
# Topics: array, binary search
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

def searchMatrix(matrix, target):
    # solution 1: simplest search. Time Complexity: O(m+n)
    # if len(matrix) == 0:
    #     return False
    # row = len(matrix) - 1
    # col = 0
    # while row >= 0 and col <= len(matrix[0]) - 1:
    #     if matrix[row][col] == target:
    #         return True
    #     elif matrix[row][col] > target:
    #         row -= 1
    #     else:
    #         col += 1
    # return False
    
    # solution 2: binary search for both rows and columns. Time Complexity: O(log(mn))
    
    if len(matrix) == 0:
        return False
    
    # careful! we need to check the columns as well! we do not need to do that in the first method.
    
    if len(matrix[0]) == 0:
        return False
    
    m = len(matrix)
    n = len(matrix[0])
    begin = 0
    end = m * n  - 1
    
    while begin + 1 < end:
        
        mid = (end - begin)// 2 + begin
        
        # careful! this is devided by n and mod by n!! we only care about the columns!
        
        if matrix[mid//n][mid%n] == target:
            return True
        
        elif matrix[mid//n][mid%n] > target:
            end = mid
            
        else:
            begin = mid
            
    return matrix[begin//n][begin%n] == target or matrix[end//n][end%n] == target