# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            return False
        else:
            if s.val == t.val:
                if self.isEqualTree(s, t):
                    return True
                else:
                    return self.isSubtree(s.left, t) | self.isSubtree(s.right, t)
            else:
                return self.isSubtree(s.left, t) | self.isSubtree(s.right, t)
    
    def isEqualTree(self, s, t):
        if s == None and t == None:
            return True
        elif s == None and t != None:
            return False
        elif s != None and t == None:
            return False
        else:
            if s.val != t.val:
                return False
            else:
                return self.isEqualTree(s.left, t.left) & self.isEqualTree(s.right, t.right)

