class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ''
        max_count = 1
        longest_palindrome = s[0]
        # 先检验形如'aabaa'这样的回文序列
        for i in range(1, len(s) - 1):
            j = 1
            while i-j >= 0 and i+j <= len(s)-1:
                if s[i-j] == s[i+j]:
                    j += 1
                else:
                    if (2*j-1) > max_count:
                        max_count = 2*j-1
                        longest_palindrome = s[i-j+1:i+j]
                    break
            if i-j < 0 and (2*j-1) > max_count:
                max_count = 2*j-1
                longest_palindrome = s[i-j+1:i+j]
            if i+j > len(s)-1 and (2*j-1) > max_count:
                max_count = 2*j-1
                longest_palindrome = s[i-j+1:i+j]

        # 再检验形如'abccba'这样的回文序列
        for i in range(0, len(s)-1):
            if s[i] != s[i+1]: continue
            j = 1
            while i-j >= 0 and i+j+1 <= len(s)-1:
                if s[i-j] == s[i+j+1]:
                    j += 1
                else:
                    if 2*j > max_count:
                        max_count = 2*j
                        longest_palindrome = s[i-j+1:i+j+1]
                    break
            if i-j < 0 and (2*j) > max_count:
                max_count = 2*j
                longest_palindrome = s[i-j+1:i+j+1]
            if i+j+1 > len(s)-1 and (2*j) > max_count:
                max_count = 2*j
                longest_palindrome = s[i-j+1:i+j+1]                
       
        return longest_palindrome
