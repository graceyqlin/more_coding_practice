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

import collections

def get_levels_for_nodes(root_node):

	node_to_level_map = collections.defaultdict(list)

	level = 0

	current_level = [root_node]

	while current_level:

		next_level = []

		for current_node in current_level:
			node_to_level_map[level].append(current_node.val)

			if current_node.left:
				next_level.append(current_node.left)

			if current_node.right:
				next_level.append(current_node.right)

			level += 1

			current_level = next_level

	

