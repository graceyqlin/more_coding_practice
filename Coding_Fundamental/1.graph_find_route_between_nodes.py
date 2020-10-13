#graph_find_route_between_nodes.py

#Topics: Graphs, DFS, BFS

# 1. Write a function that takes a directed graph with integer nodes and finds whether 
# there is a  route between two nodes.
#     - do this with BFS
#     - do this with DFS

tree_graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'C'],
  'C' : ['F'],
  'D' : [],
  'E' : ['G'],
  'F' : [],
  'G' : []
}

# def find_route_bfs(graph, node1, node2):
#     queue = []
#     visited = set()
    
#     queue.append(node1)
#     visited.add(node1)
    
#     while queue:
#         current_node = queue.pop(0)
#         next_node_list = graph[current_node]
#         for next_node in next_node_list:
#             if next_node not in visited:
#                 visited.add(next_node)
#                 queue.append(next_node)
    
#     # print(visited)
    
#     return node2 in visited

# def find_route_dfs(graph, node1, node2):
#     stack = []
#     visited = []
    
#     stack.append(node1)
    
#     while stack:
        
#         current_node = stack.pop()

#         if current_node not in visited:
#         	# visited.append(current_node)
#             next_node_list = graph[current_node]
#             for next_node in next_node_list:
#                 if next_node not in visited:
#                     stack.append(next_node)
#             visited.append(current_node)

#     # print(visited)
     
#     return node2 in visited

# find route dfs recursive
# Purpose
# find if the target node is in the subtree rooted at source node
#   if the target is in any of the subtrees rooted at children nodes -> True
#   if the target is NOT in any of the subtrees rooted at children nodes -> False

def find_route_dfs_recursive(graph, visiting_node, target_node, visited):
    print('RECURSE', node1, node2, visited)
    if node1 == node2: return True
    if node1 not in visited:
        visited.add(node1)
        for next_node in graph[node1]:
            node_exists = find_route_dfs_recursive(graph, next_node, node2, visited)
            if node_exists: return True
    return False




    # if not node1:
    #     return
    # visited.append(node1)
    # next_node_list = graph[node1]

    # while next_node_list:
    #     node1 = next_node_list.pop(0)
    #     find_route_dfs_recursive(graph, node1, node2, visited)




node1 = 'A'
node2 = 'C'
visited = set()
graph = tree_graph
print(find_route_dfs_recursive(graph, node1, node2, visited))
print(visited)







