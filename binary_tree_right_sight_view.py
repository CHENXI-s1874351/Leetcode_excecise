# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        # Depth-first search
        
        nodes_see = []
        depth_met = -1
        
        stack = [(root, 0)]
        
        while stack:
            
            node, depth = stack.pop()
            
            if node is not None:
            
                if depth > depth_met:
                    depth_met = depth
                    nodes_see.append(node.val)

                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
            
        return nodes_see

        

        # Breadth-first search
        '''
        nodes_see = {}
        
        queue = [(root, 0)]
        
        while queue:
            
            node, depth = queue.pop(0)
            
            if node is not None:
            
                nodes_see[depth] = node.val
                    
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
            
        return nodes_see.values()'''


