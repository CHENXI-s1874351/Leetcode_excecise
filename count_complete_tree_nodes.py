# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        def countLayers(root_node):
            
            count_layers = 1
            while root_node.left:
                root_node = root_node.left
                count_layers += 1
            return count_layers
        
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        elif root.left is not None and root.right is None:
            return 2
        
        else:        
        
            left_layers = countLayers(root.left)
            right_layers = countLayers(root.right)

            if left_layers == right_layers:            
                return 2 ** left_layers + self.countNodes(root.right)            

            else:
                return 2 ** right_layers + self.countNodes(root.left)