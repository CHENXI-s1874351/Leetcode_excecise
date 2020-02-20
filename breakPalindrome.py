class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ''
        mid = len(palindrome) // 2
        pre = 0
        while pre < mid:
            if palindrome[pre] != 'a':
                return palindrome[:pre] + 'a' + palindrome[pre+1:]
            pre += 1   
        return palindrome[:-1] + 'b'
