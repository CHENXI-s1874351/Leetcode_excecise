class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        #s[0::] = s[::-1]
        
        i = 0
        j = len(s) - i - 1
        
        while i < j:
            
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j = len(s) - i - 1
            
            