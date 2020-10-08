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


def get_levels_for_nodes(root_node):
    import collections
    
    if root_node is None:
        return []
    
    node_to_level_map = collections.defaultdict(list)
    
    nodes_at_current_level = [head_node]
    
    level = 0
    
    while nodes_at_current_level:        
        
        nodes_at_next_level = []
        
        for current_node in nodes_at_current_level:
            node_to_level_map[level].append(current_node.val)
            
            
            if current_node.left:
                nodes_at_next_level.append(current_node.left)
            
            if current_node.right:
                nodes_at_next_level.append(current_node.right)
        
        nodes_at_current_level = nodes_at_next_level
        level += 1
        
        
    return node_to_level_map

print(get_levels_for_nodes(t1))

def get_levels_for_nodes_with_dfs(root_node):
    pass

def get_levels_for_nodes_in_dag(root_node):
    pass
        
