class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        for i in range(0, len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]: continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                diff = abs(target - (nums[i] + nums[l] + nums[r]))
                if diff < min_diff:
                    min_diff = diff
                    output = [nums[i], nums[l], nums[r]]
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                elif nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return sum(output)
