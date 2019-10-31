class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        temp = []
        self.backtrack(temp, nums, results)
        return results
    
    def backtrack(self, temp, nums, results):
        
        if nums == []:
            if temp not in results:
                results.append(temp[:])
        
        else:
            for i in range(len(nums)):
                temp.append(nums[i])
                self.backtrack(temp, nums[0:i] + nums[i+1:], results)
            
        if temp:
            temp.pop()
            