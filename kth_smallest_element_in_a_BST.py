# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        # First use Breadth-first search to store every element,
        # then use sorted() method to get the kth smallest element.
        node_values = []
        
        queue = [root]
        
        while queue:
            
            node = queue.pop(0)
            
            if node is not None:
                node_values.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        sorted_values = sorted(node_values)
        return sorted_values[k-1]


        # Solution above doesn't use the fact that it is a binary search tree.
        # Instead it considers the tree as a normal binary tree.
        # We can use LDR to polish the solution.

        '''
        res = 0
        def f(node):
            nonlocal res, k
            if node.left:
                f(node.left)
                
            k -= 1
            if k == 0:
                res = node.val
                return
            if node.right:
                f(node.right)
        
        f(root)
        return res'''