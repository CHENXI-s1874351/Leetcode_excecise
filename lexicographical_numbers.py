class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        '''
        # 相当于把数字转化成字符串，然后用字符串排序
        alist = list(range(1, n+1))
        alist.sort(key = str)       
        return alist        
        '''
        
        # 先序遍历10叉树
        tree = [i for i in range(9, 0, -1) if i <= n]
        alist = []
        while tree:
            num = tree.pop()
            alist.append(num)
            for i in range(num*10+9, num*10-1, -1):
                if i <= n:
                    tree.append(i)
        return alist
        
        
        
        
        
