class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dict_ = {}
        for i in nums:
            try:
                dict_[i] += 1
            except:
                dict_[i] = 1
                
        for key in dict_:
            if dict_[key] == 1:
                return key
    


    # Code below is a solution using bit operation.
    # Details can be seen on 
    # https://leetcode-cn.com/problems/single-number-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--31/
    # This solution does not need extra storage.

        '''x1 = 0
        x2 = 0
        mask = 0
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask

        return x1'''
