class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        '''
        dict = {}
        for i in nums:
            
            try:
                dict.pop(i)
            except:
                dict[i] = i
            
        return dict.popitem()[0]'''

        # Codes above utilize hash table to solve the problem.
        # Its time complexity is O(n) and it uses extra storage space.


        # We can also exploit XOR operation to solve this problem.
        # a ^ a = 0; a ^ 0 = a
        # No extra storage space needed.

        answer = 0
        
        for num in nums:
            
            answer = answer ^ num
        
        return answer