#LC110.Balanced_Binary_Tree.py

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.

# time complexity: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def isBalanced(self, root: TreeNode):
    if not root:
        return True
    
    def get_height(root):
        if not root:
            return 0
        return max(get_height(root.left), get_height(root.right)) + 1
    
    if abs(get_height(root.left) - get_height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
        return True
    return False


t1 = TreeNode(val = 1)
t2 = TreeNode(val = 2)
t3 = TreeNode(val = 3)
t4 = TreeNode(val = 4)
t5 = TreeNode(val = 5)
t6 = TreeNode(val = 6)

t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5
t5.left = t6

s = Solution()
print(s.isBalanced(t1))
