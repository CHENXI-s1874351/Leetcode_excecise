class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        lastPos = n-1
        for i in range(n-2, -1, -1):
            if nums[i] + i >= lastPos:
                lastPos = i
        if lastPos == 0:
            return True
        else:
            return False