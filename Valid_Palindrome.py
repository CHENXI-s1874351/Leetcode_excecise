class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1 : return True
        else:
            s = list(s)
            while len(s) >= 2:
                pre = s.pop(0).lower()
                lat = s.pop(-1).lower()
                while pre.isalnum() != True:
                    if len(s) == 0: return True
                    pre = s.pop(0).lower()
                while lat.isalnum() != True:
                    if len(s) == 0: return True
                    lat = s.pop(-1).lower()
                if pre != lat:
                    return False
            return True
                


