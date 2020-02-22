# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        maxCount = 0
        arr = [] # 用于存储节点的值
        counts = [0] # 用于存储对应节点的层数
        stack = [root]
        while stack:
            node = stack.pop()
            count = counts.pop()
            if count == maxCount:
                arr.append(node.val)
            elif count > maxCount:
                arr = [node.val]
                maxCount = count
            if node.right:
                stack.append(node.right)
                counts.append(count + 1)
            if node.left:
                stack.append(node.left)
                counts.append(count + 1)
        return sum(arr)
