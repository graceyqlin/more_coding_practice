# 8. You receive a tree. Print all the nodes and their level from the root
# You receive a tree. Print all the nodes and their level from the root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
t1 = TreeNode(val = 1)
t2 = TreeNode(val = 2)
t3 = TreeNode(val = 3)
t4 = TreeNode(val = 4)
t5 = TreeNode(val = 5)
t6 = TreeNode(val = 6)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.right = t6


# def get_levels_for_nodes(root_node):
#     import collections
    
#     if root_node is None:
#         return []
    
#     node_to_level_map = collections.defaultdict(list)
    
#     nodes_at_current_level = [root_node]
    
#     level = 0
    
#     while nodes_at_current_level:        
        
#         nodes_at_next_level = []
        
#         for current_node in nodes_at_current_level:
#             node_to_level_map[level].append(current_node.val)
            
            
#             if current_node.left:
#                 nodes_at_next_level.append(current_node.left)
            
#             if current_node.right:
#                 nodes_at_next_level.append(current_node.right)
        
#         nodes_at_current_level = nodes_at_next_level
#         level += 1
        
        
#     return node_to_level_map

# print(get_levels_for_nodes(t1))

# def get_levels_for_nodes_with_dfs(root_node):
#     import collections

#     node_to_level_map = collections.defaultdict(list)

#     level = 0   

#     def get_vals(node, level, output):

#         if node is None:
#             return 

#         output[level].append(node.val)
        
#         get_vals(node.left, level +1, output)
        
#         get_vals(node.right, level +1, output)

#     get_vals(root_node, level, node_to_level_map)

#     return node_to_level_map
 
# print(get_levels_for_nodes_with_dfs(t1))   


cross_edge_graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'C'],
  'C' : ['F'],
  'D' : [],
  'E' : ['G'],
  'F' : [],
  'G' : []
}
    

def get_levels_for_nodes_in_dag(graph, root_node):
   
    import collections
    
    if root_node is None:
        return []
    
    node_to_level_map = collections.defaultdict(list)
    
    nodes_at_current_level = [root_node]
    
    level = 0
    
    while nodes_at_current_level:        
        nodes_at_next_level = []
        for current_node in nodes_at_current_level:
            node_to_level_map[level].append(current_node)
            
            nodes_at_next_level += [i for i in graph[current_node]]
        
        nodes_at_current_level = nodes_at_next_level

        level += 1
        
        
    return node_to_level_map

print(get_levels_for_nodes_in_dag(cross_edge_graph, 'A'))
        
