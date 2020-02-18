# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root: return None
        else: return self.postOrderTraversal(root, target)
    
    # 这道题目用后序排序就可以完美解决
    def postOrderTraversal(self, root, target):
        if root.left:
            root.left = self.postOrderTraversal(root.left, target)
        if root.right:
            root.right = self.postOrderTraversal(root.right, target)
        if not root.left and not root.right:
            if root.val == target:
                return None
        return root

        