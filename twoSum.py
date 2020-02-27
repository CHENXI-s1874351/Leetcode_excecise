class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = [i]
            else:
                hash_map[nums[i]].append(i)
        
        for i in range(len(nums)):
            num = nums[i]
            remain = target - num
            if remain in hash_map:
                for value in hash_map[remain]:
                    if i != value:
                        return [i, value]