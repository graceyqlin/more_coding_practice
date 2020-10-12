# Create_Linked_List_From_Tree.py

# 2. Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.

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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_levels_for_nodes(root_node):
    import collections
    
    if root_node is None:
        return []
    
    node_to_level_map = collections.defaultdict(list)
    
    nodes_at_current_level = [root_node]
    
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


def get_linked_list_from_tree(root_node):

	node_to_level_map = get_levels_for_nodes(root_node)

	dummy = current_list_node = ListNode(0)

	for level in node_to_level_map:
		for node_val in node_to_level_map[level]:
			current_list_node.next = ListNode(node_val)
			current_list_node = current_list_node.next

	return dummy.next

print(get_linked_list_from_tree(t1))

test = get_linked_list_from_tree(t1)

while test:
	print(test.val)
	test = test.next
