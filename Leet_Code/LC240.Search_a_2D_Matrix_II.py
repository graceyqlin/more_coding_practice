# LC240.Search_a_2D_Matrix_II.py

# Topics: array

# Be careful of the difference between this one and LC74.Search_a_2D_Matrix.py

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.


def searchMatrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # Time complexity: O(m+n)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        row = m-1
        col = 0
        while col < n and row >=0:
            if matrix[row][col] == target:
                return True 
            if matrix[row][col] > target:
                row += -1
            else:
                col += 1
        return False
                
