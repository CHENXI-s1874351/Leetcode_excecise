# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 0: return []
        elif N == 1: return [TreeNode(0)]
        else:
            output = []
            for i in range(1, N-1):    
                if i % 2 == 1:
                    for left_node in self.allPossibleFBT(i):
                        for right_node in self.allPossibleFBT(N-i-1):
                            root = TreeNode(0)
                            root.left = left_node
                            root.right = right_node
                            output.append(root)
            return output
