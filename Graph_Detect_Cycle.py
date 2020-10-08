# Write a program that detects if there is a cycle in a graph

def detect_cycle_bfs(graph):
    queue = []
    visited = []
    queue.append(list(graph.keys())[0])
    
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for next_node in graph[current_node]:
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
            else:
                return 'bfs detect. the graph has cycle'
            
    return 'bfs detect. the graph has no cycle'


                
    
def detect_cycle_dfs(graph):
    stack = []
    visited = []
    
    stack.append(list(graph.keys())[0])
    
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            # visited.append(current_node)
            for next_node in graph[current_node]:
                if next_node not in visited:
                    stack.append(next_node)
                else:
                    return 'dfs detect. the graph has cycle'
            visited.append(current_node)
            
        else:
            
            return 'dfs detect. the graph has cycle'
        
    return 'dfs detect. the graph has no cycle'
                    
  
