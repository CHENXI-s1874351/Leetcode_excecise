# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        arr = []
        sum_ = self.preOrderTraversal(root, arr)
        max_value = 0
        for i in arr:
            product = i  * (sum_ - i)
            max_value = max(max_value, product)
        return max_value % (10**9+7)
            
    def preOrderTraversal(self, root, arr):
        sum_ = root.val
        if root.left:
            left_val = self.preOrderTraversal(root.left, arr)
            sum_ += left_val
            arr.append(left_val)
        if root.right:
            right_val = self.preOrderTraversal(root.right, arr)
            sum_ += right_val
            arr.append(right_val)
        return sum_   