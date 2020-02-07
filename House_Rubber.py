class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums[0], nums[1])
        else:
            a1 = nums[0]
            a2 = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                if nums[i] + a1 >= a2:
                    temp = a1
                    a1 = a2
                    a2 = nums[i] + temp
                else:
                    a1 = a2
                # 这一段也可以写成如下形式
                '''
                temp = a1
                a1 = a2
                a2 = max(a2, nums[i] + temp)
                '''

            return a2

