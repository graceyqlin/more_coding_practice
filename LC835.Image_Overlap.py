#LC835.Image_Overlap

# You are given two images img1 and img2 both of size n x n, 
# represented as binary, square matrices of the same size. 
# (A binary matrix has only 0s and 1s as values.)

# We translate one image however we choose (sliding it left, right, up,
# or down any number of units), and place it on top of the other image. 
# fter, the overlap of this translation is the number of positions that 
# ave a 1 in both images.

# (Note also that a translation does not include any kind of rotation.)

# What is the largest possible overlap?
# Example:
# Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], 
# img2 = [[0,0,0],[0,1,1],[0,0,1]]
# Output: 3

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        def find_1_index(matrix):
            index = []
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 1:
                        index.append([i,j])
            return index
        
        A_1_index = find_1_index(A)
        B_1_index = find_1_index(B)
        
        difference_index_dic = collections.defaultdict(int)
        
        ans = 0
        
        for a in A_1_index:
            for b in B_1_index:
                difference_index = (b[0]-a[0], b[1]-a[1])
                
                difference_index_dic[difference_index] += 1
                
                ans = max(ans, difference_index_dic[difference_index])
        return ans