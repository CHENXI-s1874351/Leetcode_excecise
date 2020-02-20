class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)+1 < n:
            return -1
        edges = [[] for i in range(n)]
        for con in connections:
            edges[con[0]].append(con[1])
            edges[con[1]].append(con[0])
        count = 0
        connected_queue = []
        used = set()
        for i in range(n):
            if i not in used:
                used.add(i)
                connected_queue.append(i)
                while connected_queue:
                    index = connected_queue.pop(0)
                    for j in edges[index]:
                        if j not in used:
                            connected_queue.append(j)
                            used.add(j)
                count += 1
        return count - 1

        # 当然除了上述的深度优先算法
        # 也可以用并查集来解决该问题
        '''
        if len(connections)+1 < n:
            return -1
        edges = [[] for i in range(n)]
        for con in connections:
            edges[con[0]].append(con[1])
            edges[con[1]].append(con[0])
        pre = [-1 for i in range(n)]
        for i in range(n):
            if pre[i] == -1:
                pre[i] = i
                used = {i}
                queue = [i]
                while queue:
                    index = queue.pop(0)
                    for j in edges[index]:
                        if j not in used:
                            queue.append(j)
                            pre[j] = i
                            used.add(j)
        return len(set(pre)) - 1
        '''

