#graph_find_route_between_nodes.py

#Topics: Graphs, DFS, BFS

# 1. Write a function that takes a directed graph with integer nodes and finds whether 
# there is a  route between two nodes.
#     - do this with BFS
#     - do this with DFS

def find_route_bfs(graph, node1, node2):
    queue = []
    visited = []
    
    queue.append(node1)
    visited.append(node1)
    
    while queue:
        current_node = queue.pop(0)
        next_node_list = graph[current_node]
        for next_node in next_node_list:
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
    
    # print(visited)
    
    return node2 in visited

def find_route_dfs(graph, node1, node2):
    stack = []
    visited = []
    
    stack.append(node1)
    
    while stack:
        
        current_node = stack.pop()

        if current_node not in visited:
        	# visited.append(current_node)
            next_node_list = graph[current_node]
            for next_node in next_node_list:
                if next_node not in visited:
                    stack.append(next_node)
            visited.append(current_node)

    # print(visited)
     
    return node2 in visited




