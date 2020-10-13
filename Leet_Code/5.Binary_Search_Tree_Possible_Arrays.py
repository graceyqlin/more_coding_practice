# 5.Binary_Search_Tree_Possible_Arrays.py

# 5. A binary search tree was created by traversing through an array from left to right and inserting each element.

#    Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
t6 = TreeNode(val = 6)
t3 = TreeNode(val = 3)
t1 = TreeNode(val = 1)
t4 = TreeNode(val = 4)
t9 = TreeNode(val = 9)
t7 = TreeNode(val = 7)
t10 = TreeNode(val = 10)
t12 = TreeNode(val = 12)

t6.left = t3
t6.right = t9
t3.left = t1
t3.right = t4
t9.right = t10
t9.left = t7
t10.left = t12



