class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(0, len(nums)-2):
            if nums[i] > 0: break
            if i >= 1 and nums[i] == nums[i-1]: continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if l > i + 1 and nums[l] == nums[l-1]: 
                    l += 1
                    continue
                if r < len(nums) - 1 and nums[r] == nums[r+1]: 
                    r -= 1
                    continue
                if nums[i] + nums[l] + nums[r] == 0:
                    output.append([nums[l], nums[i], nums[r]])
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return output

        
