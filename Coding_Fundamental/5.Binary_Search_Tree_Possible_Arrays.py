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


# from binarytree import  Node, bst, pprint

def weave_list(first_list, second_list, weaved, prefix):

    if not first_list or not second_list:
       tmp = []
       tmp += prefix

       if first_list:
          tmp += first_list

       if second_list:   
          tmp += second_list

       weaved.append(tmp)

       return

    if first_list:
        fitem_first_list = first_list.pop(0)
        prefix.append(fitem_first_list)
        weave_list(first_list, second_list, weaved, prefix)

        prefix.pop()
        first_list.insert(0, fitem_first_list)

    if second_list:
        fitem_second_list = second_list.pop(0)
        prefix.append(fitem_second_list)
        weave_list(first_list, second_list, weaved, prefix)

        prefix.pop()
        second_list.insert(0, fitem_second_list)        


def allsequences(root):
    result = []
    if root == None:
       return result

    prefix = []
    prefix.append(root.val)

    left = allsequences(root.left) or [[]]
    right = allsequences(root.right) or [[]]
    

    for i in range(len(left)):
        for j in range(len(right)):
            weaved = []
            weave_list(left[i], right[j], weaved, prefix)

        result += weaved

    return result


print(allsequences(t6))


