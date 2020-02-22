class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hash_map = {}
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in hash_map:
                hash_map[size] = [[i]]
            else:
                groups = hash_map[size]
                if len(groups[-1]) == size:
                    hash_map[size].append([i])
                else:
                    hash_map[size][-1].append(i)

        output = []
        for key in hash_map:
            for arr in hash_map[key]:
                output.append(arr)
                
        return output