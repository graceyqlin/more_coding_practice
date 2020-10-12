# Write a program that detects if there is a cycle in a graph

# def detect_cycle(graph， current_node):
#     if not current_node:
#         return

cross_edge_graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'C'],
  'C' : ['A', 'F'],
  'D' : [],
  'E' : ['G'],
  'F' : [],
  'G' : []
}

def get_next_val(graph, current_node, directions, cycle_indicator): 
    # if not current_node:
    #     return directions

    
    directions.append(current_node)

    if len(directions) > 20:
        cycle_indicator = True
        print(cycle_indicator)
        # return cycle_indicator
        return 'there is a cycle'


    next_node_list = graph[current_node]
    for next_node in next_node_list:
        get_next_val(graph, next_node, directions, cycle_indicator)

directions = []
num_run = 0
cycle_indicator = False
print(get_next_val(cross_edge_graph, 'A', directions, cycle_indicator)) 
print(cycle_indicator)
print(directions)
# print(num_run)


    

                
    
# def detect_cycle_dfs(graph):
#     stack = []
#     visited = []
    
#     stack.append(list(graph.keys())[0])
    
#     while stack:
#         current_node = stack.pop()
#         if current_node not in visited:
#             # visited.append(current_node)
#             for next_node in graph[current_node]:
#                 if next_node not in visited:
#                     stack.append(next_node)
#                 else:
#                     return 'dfs detect. the graph has cycle'
#             visited.append(current_node)
            
#         else:
            
#             return 'dfs detect. the graph has cycle'
        
#     return 'dfs detect. the graph has no cycle'
                    
  
