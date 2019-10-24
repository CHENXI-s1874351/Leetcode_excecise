class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()        
        new_sentence = ""
        
        
        for word in words:
            
            new_sentence += word[::-1] + ' '
        
        return new_sentence[:-1]