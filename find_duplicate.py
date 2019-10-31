class Solution:
    def findDuplicate(self, nums):
        
        # 创建快慢指针并找到其相遇点
        quick = nums[0]
        slow = nums[0]
        
        while True:
            quick = nums[nums[quick]]
            slow = nums[slow]
            if quick == slow:
                break
        
        # 找到循环的入口
        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]
        
        return finder
