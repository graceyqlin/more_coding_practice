#LC200.Number_Of_Islands.py

#Topic: dfs, bfs

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

#dfs:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        cnt = 0
        
        def dfs(grid, i, j):
            for (x,y) in [(0,1), (0,-1), (1,0), (-1,0)]:
                if 0 <= i+x < len(grid) and 0 <= y + j < len(grid[0]) and grid[i+x][y+j] == '1':
                    grid[i+x][y+j] = '0'
                    dfs(grid, i+x, y+j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(grid, i, j)
        
        return cnt



#bfs:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs
        import collections
        cnt = 0
        queue = collections.deque([])
        
        def bfs(grid, i, j):
            while queue:
                i, j = queue.popleft()
                for (x,y) in [(0,1), (0,-1), (1,0), (-1,0)]:
                    if 0 <= i+x < len(grid) and 0 <= y + j < len(grid[0]) and grid[i+x][y+j] == '1':
                        grid[i+x][y+j] = '0'
                        queue.append((i+x, j+y))
                    
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':    
                    queue.append((i,j))
                    cnt += 1
                    bfs(grid, i, j)
                    
        return cnt
        
