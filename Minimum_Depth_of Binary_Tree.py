# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        depth_list = []
        self.minDepth_(root, 1, depth_list)
        return min(depth_list)
    
    def minDepth_(self, root, num, depth_list):
        if root.left == None and root.right == None:
            depth_list.append(num)

        else:
            num += 1
            if root.left:
                self.minDepth_(root.left, num, depth_list)
            if root.right:
                self.minDepth_(root.right, num, depth_list)

