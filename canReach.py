class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0: return True
        visited = set()
        queue = [start]
        while queue:
            index = queue.pop(0)
            if index - arr[index] >= 0:
                if arr[index-arr[index]] == 0:
                    return True
                else:
                    if index-arr[index] not in visited:
                        visited.add(index-arr[index])
                        queue.append(index-arr[index])
            if index + arr[index] <= len(arr)-1:
                if arr[index+arr[index]] == 0:
                    return True
                else:
                    if index+arr[index] not in visited:
                        visited.add(index+arr[index])
                        queue.append(index+arr[index])
        return False
