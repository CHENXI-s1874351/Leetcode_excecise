# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        max_ = max(nums)
        index_ = nums.index(max_)
        tree_node = TreeNode(max_)
        
        if nums[0:index_]:
            tree_node.left = self.constructMaximumBinaryTree(nums[0:index_])
        else:
            tree_node.left = None
        
        if nums[index_+1:]:
            tree_node.right = self.constructMaximumBinaryTree(nums[index_+1:])
        else:
            tree_node.right = None
        
        return tree_node