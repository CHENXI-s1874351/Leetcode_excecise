class Solution:
    def findTheCity(self, n: int, edges: 'List[List[int]]', distanceThreshold: int) -> int:
        adjacency_matrix = [[10001 for i in range(n)] for j in range(n)]
        for edge in edges:
            f, t, weight = edge
            adjacency_matrix[f][t] = weight
            adjacency_matrix[t][f] = weight
        for i in range(n):
            adjacency_matrix[i][i] = 0
        # 至此，邻接矩阵初始化完毕
        # 在邻接矩阵中每个城市到自己的距离是0
        # 如果在edges数组中直接相邻，则初始化的值为weight
        # 如果在edges数组中不直接相邻，则初始化的值为10001
        # (因为题目中说weight最大值为10000)
        for i in range(n):
            not_city_list = [j for j in range(n) if j != i]
            for j in range(n-1):
                min_dis = 10001
                index = n
                for m in not_city_list:
                    if adjacency_matrix[i][m] < min_dis:
                        min_dis = adjacency_matrix[i][m]
                        index = m

                # 如果min_dis等于10001，说明剩下的节点全是不连通的
                # 可以直接跳出本轮循环
                if min_dis == 10001: break

                # 用这次新找到的节点去更新最短路的权重
                not_city_list.remove(index)
                for m in not_city_list:
                    temp = adjacency_matrix[i][index] + adjacency_matrix[index][m]
                    if adjacency_matrix[i][m] > temp:
                        adjacency_matrix[i][m] = temp
                        adjacency_matrix[m][i] = temp

        # 在邻接矩阵的所有最短路都更新完后，统计哪个城市连通节点是最少的
        index = 0
        min_count = n+1
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and adjacency_matrix[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_count:
                min_count = count
                index = i
        return index