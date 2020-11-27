# LC337.House_Robber_III.py
# Topics: dynamic programming, tree, depth first search
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Example 1:

# Input: [3,2,3,null,3,null,1]

#      3
#     / \
#    2   3
#     \   \ 
#      3   1

# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.


def get_max_rob_value(node):
	def sub_rob(node):
		if not node:
			return (0,0)
		left = sub_rob(node.left)
		right = sub_rob(node.right)
		# rob current node and can only rob the one next to left, or right
		rob_current = node.val + left[1] + right[1]
		# rob the next node:
		rob_next = max(left[0], left[1]) + max(right[0], right[1])

		return (rob_current, rob_next)

	return max(sub_rob(node))

