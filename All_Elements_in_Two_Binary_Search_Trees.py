# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1, list2 = [], []
        output = []
        self.preOrderTraversal(root1, list1)
        self.preOrderTraversal(root2, list2)
        index1, index2 = 0, 0
        while index1 <= len(list1) -1 and index2 <= len(list2) -1:
            if list1[index1] <= list2[index2]:
                output.append(list1[index1])
                index1 += 1
            else:
                output.append(list2[index2])
                index2 += 1
        if index1 == len(list1):
            for i in range(index2, len(list2)):
                output.append(list2[i])
        else:
            for i in range(index1, len(list1)):
                output.append(list1[i])
        return output

    def preOrderTraversal(self, root, values):
        if root == None:
            return
        else:
            self.preOrderTraversal(root.left, values)
            values.append(root.val)
            self.preOrderTraversal(root.right, values)
        