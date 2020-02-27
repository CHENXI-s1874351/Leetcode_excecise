class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        nums.sort()
        output = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]: continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if l > j + 1 and nums[l] == nums[l-1]: 
                        l += 1
                        continue
                    if r < len(nums) - 1 and nums[r] == nums[r+1]:
                        r -= 1
                        continue
                    if (nums[i] + nums[j] + nums[l] + nums[r]) == target:
                        output.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
        return output