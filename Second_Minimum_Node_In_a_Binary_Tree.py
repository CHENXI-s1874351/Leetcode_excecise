# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        root_val = root.val
        value_list = [root.val]
        node_list = [root]
        while len(node_list) != 0:
            node = node_list.pop(0)
            if node.val != root_val:
                if len(value_list) == 1:
                    value_list.append(node.val)
                else:
                    if node.val < value_list[1]:
                        value_list[1] = node.val
            else:
                if node.left != None:
                    node_list.append(node.left)
                    node_list.append(node.right)
        if len(value_list) == 1: return -1
        else: return value_list[1]


        