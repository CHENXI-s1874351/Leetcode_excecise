class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        quotient = len(s) // (2 * k)
        reminder = len(s) % (2 * k)
        
        i = 0
        new_s = ''
        
        while i < quotient:
            
            new_s += s[i*2*k: (i+1)*2*k-k][::-1]
            new_s += s[(i+1)*2*k-k: (i+1)*2*k]
            i += 1
        
        if reminder < k:
            new_s += s[i*2*k:][::-1]
        else:
            new_s += s[i*2*k: (i+1)*2*k-k][::-1]
            new_s += s[(i+1)*2*k-k:]
        
        return new_s
        