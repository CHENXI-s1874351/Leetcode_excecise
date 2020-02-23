class Solution:
    def jump(self, nums: List[int]) -> int:
        # 这道题目很简单，在每一步里选择最大的数字跳就行
        # 题目里说“假设你总是可以到达数组的最后一个位置”
        # 说明nums里面没有为0的元素
        # 为什么呢？
        # 因为选择的走法可以是每次只走一步，这样也“可以到达数组的最后一个位置”
        # 因此nums里面没有为0的元素
        if len(nums) == 1: return 0
        count = 0
        index = 0
        while True:
            if index+nums[index] >= len(nums)-1:
                return count+1
            max_ = nums[index+1] + index+1
            for i in range(index+1, index+nums[index]+1):
                if nums[i] + i >= max_:
                    max_ = nums[i] + i
                    index = i
            count += 1