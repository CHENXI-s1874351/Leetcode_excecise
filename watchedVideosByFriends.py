class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(watchedVideos)
        adjacency_matrix = [[101 for j in range(n)] for i in range(n)]
        for i in range(n):
            adjacency_matrix[i][i] = 0
        for i in range(n):
            for friend in friends[i]:
                adjacency_matrix[i][friend] = 1
                adjacency_matrix[friend][i] = 1
        
        not_visited_list = [i for i in range(n)]
        not_visited_list.remove(id)
        while True:
            min_dis = 101
            for i in not_visited_list:
                if adjacency_matrix[id][i] < min_dis:
                    min_dis = adjacency_matrix[id][i]
                    index = i
            
            if min_dis > level:
                break
            
            not_visited_list.remove(index)
            for i in not_visited_list:
                if adjacency_matrix[id][i] > adjacency_matrix[id][index] + adjacency_matrix[index][i]:
                    adjacency_matrix[id][i] = adjacency_matrix[id][index] + adjacency_matrix[index][i]
                    adjacency_matrix[i][id] = adjacency_matrix[id][index] + adjacency_matrix[index][i]
        
        arr = []
        for i in range(n):
            if adjacency_matrix[id][i] == level:
                arr.append(i)
        
        videos_frequency_dict = {}
        for i in arr:
            videos = watchedVideos[i]
            for v in videos:
                if v in videos_frequency_dict:
                    videos_frequency_dict[v] += 1
                else:
                    videos_frequency_dict[v] = 1
        
        output = list(videos_frequency_dict.items())
        # 如果需要一列升序，相同值按照另一列降序，可以写成
        # output.sort(key = lambda x: (x[1], -x[0]))
        output.sort(key = lambda x: (x[1], x[0]))

        return [i[0] for i in output]







            
