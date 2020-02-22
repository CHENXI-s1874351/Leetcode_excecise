class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # 如果数组长度不能被k整除，那肯定不能完全划分
        if len(nums) % k != 0: return False
        # 先利用哈希表统计每个数字出现的频率
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        # 然后根据key的值从小到大排列哈希表        
        arr = list(d.items())
        arr.sort(key = lambda x: x[0])
        # 需要把不可变的元组转换成可变的列表
        for i in range(len(arr)):
            arr[i] = list(arr[i])
        # 针对从小到大排列的哈希表来说
        # 如果某个元素出现了m次，那么其之后的k-1个元素也至少要出现m次
        for i in range(len(arr)-k+1):
            if arr[i][1] != 0:
                for j in range(k-1, -1, -1):
                    if arr[i+j][1] >= arr[i][1] and arr[i+j][0] - j == arr[i][0]:
                        arr[i+j][1] -= arr[i][1]
                    else:
                        return False
        # 如果剩下的len(arr)-k+1个元素中有不为0的，
        # 说明不能完全划分
        for i in range(len(arr)-k+1, len(arr)):
            if arr[i][1] != 0:
                return False
                
        return True
