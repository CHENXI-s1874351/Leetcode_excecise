class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        d_t = {}
        for i in t:
            if i in d_t:
                d_t[i] += 1
            else:
                d_t[i] = 1
        for i in d:
            if i not in d_t:
                count += d[i]
            else:
                if d[i] > d_t[i]:
                    count += d[i] - d_t[i]
        return count

