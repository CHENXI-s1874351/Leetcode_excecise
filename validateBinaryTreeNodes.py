class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # 形成一颗有效二叉树的充分必要条件
        # 首先每个节点最多只能有一个父母节点
        # 其次有父母节点的node数必须等于n-1
        node = {}

        for i in leftChild:
            if i == -1:
                continue
            if i in node:
                return False
            else:
                node[i] = 1

        for i in rightChild:
            if i == -1:
                continue
            if i in node:
                return False
            else:
                node[i] = 1
        
        if len(node) != n - 1:
            return False

        return True