# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        arr = []

        def traversal(root, arr, flag):
            if not root.left and not root.right:
                return 
            if root.left:
                if flag:
                    arr.append(root.left.val)
                if root.val % 2 == 0:
                    traversal(root.left, arr, True)
                else:
                    traversal(root.left, arr, False)
            if root.right:
                if flag:
                    arr.append(root.right.val)
                if root.val % 2 == 0:
                    traversal(root.right, arr, True)
                else:
                    traversal(root.right, arr, False)
        
        if root.val % 2 == 0:
            flag = True
        else:
            flag = False
        
        if root.left:
            traversal(root.left, arr, flag)
        if root.right:
            traversal(root.right, arr, flag)
        
        return sum(arr)

