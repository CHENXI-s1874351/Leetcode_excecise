class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        l = 0
        r = 1
        max_count = 1
        arr = [s[0]]
        while r <= len(s) - 1:
            if s[r] not in arr:
                arr.append(s[r])
                r = r + 1
                if r - l > max_count:
                    max_count = r - l
            else:
                arr.pop(0)
                l += 1
        return max_count