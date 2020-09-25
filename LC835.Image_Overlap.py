#LC835.Image_Overlap
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