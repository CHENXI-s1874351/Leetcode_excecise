class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        dict = {}
        
        for num in nums:
            try:
                dict.pop(num)
            except:
                dict[num] = num
        
        return [dict.popitem()[0], dict.popitem()[0]]

        # Solution above using extra space to solve the problem.
        # If we make use of bit operation like previous two questions,
        # we don't need extra space and the time complexity can still be
        # limitted to O(n).

        # Detailed description of the solution below can be seen on 
        # http://liadbiz.github.io/leetcode-single-number-problems-summary/


        '''

        # First we get which bit should be used to divide two groups.
        sign = 0
        for num in nums:
            sign ^= num
        
        sign = sign & (~sign + 1)
        
        # Then we use "sign" to divide two groups.
        # In each group, there is only one number that occurs one time and the rests occur twice.
        
        r1 = 0
        r2 = 0
        
        for num in nums:
            if num & sign == 0:
                r1 ^= num
            else:
                r2 ^= num
        
        return [r1, r2]
                
        '''