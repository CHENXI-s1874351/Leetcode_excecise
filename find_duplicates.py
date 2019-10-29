class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 0:
            return nums
        
        for i in range(len(nums)):
            
            while nums[nums[i] - 1] != nums[i]:
                
                i1 = nums[i] - 1
                nums[i] ^= nums[i1]
                nums[i1] ^= nums[i]
                nums[i] ^= nums[i1]
        
        repeated_elements = []
        for i in range(len(nums)):          
            if i != nums[i] - 1:
                repeated_elements.append(nums[i])
                
        return repeated_elements
            
                
                