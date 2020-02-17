class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if not arr: return 0
        count = 0
        p = [0]
        for i in arr:
            p.append(p[-1] + i)
        for i in range(len(p)-k):
            sum_ = p[i+k] - p[i]
            if sum_ >= threshold * k:
                count += 1
        return count