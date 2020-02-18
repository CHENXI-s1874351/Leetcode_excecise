class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        n = len(arr)
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        a = []
        max_ = 0
        for i in d:
            a.append(d[i])
            if d[i] > max_:
                max_ = d[i]
        # 形成频率数组，然后只需要对该数组进行排序即可
        # 这里如果使用冒泡排序会超时(O(n^2))
        # 因此使用桶排序(O(n))
        fre_arr = [0 for i in range(max_+1)]
        for i in a:
            fre_arr[i] += 1
        sum_ = 0
        count = 0
        for i in range(len(fre_arr)-1, 0, -1):
            if fre_arr[i] > 0:
                for j in range(fre_arr[i]):
                    sum_ += i
                    count += 1
                    if sum_ >= n//2:
                        return count