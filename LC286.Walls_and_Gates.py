#LC286.Walls_and_Gates.py
# Topic: dfs, bfs
# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example: 

# Given the 2D grid:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

 # dfs
        def dfs(rooms, r, c):
            for (x,y) in [(-1,0), (0, 1), (1,0), (0, -1)]:
                if 0 <= r+x < len(rooms) and 0 <= c+y < len(rooms[0]) and rooms[r+x][c+y] > rooms[r][c]:
                    rooms[r+x][c+y] = rooms[r][c] + 1
                    dfs(rooms, r+x, c+y)
                    
        if not rooms:
            return []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    dfs(rooms, r, c)



#         # bfs
        import collections
        
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        
        queue = collections.deque([])
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i,j))
                    
        
        while queue:
            current_r, current_c = queue.popleft()
            for change_r, change_c in directions:
                new_r = current_r + change_r
                new_c = current_c + change_c
                if 0 <= new_r < len(rooms) and 0 <= new_c < len(rooms[0]) and rooms[new_r][new_c] > rooms[current_r][current_c]:                
                    rooms[new_r][new_c] = rooms[current_r][current_c] + 1
                    queue.append((new_r, new_c))
                
                    