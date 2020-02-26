class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        r = 3
        dict_ = {'a': 0, 'b': 0, 'c': 0}
        for i in s[0:3]:
            dict_[i] += 1
        count = 0

        while True:
            while 0 in dict_.values():
                if r > len(s) - 1: 
                    return count
                dict_[s[r]] += 1
                r += 1
            
            count += len(s)-r+1
            dict_[s[l]] -= 1
            l += 1