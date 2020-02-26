class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        met = {}
        for i in range(len(s)-minSize+1):
            string = s[i:i+minSize]
            if len(set(string)) > maxLetters:
                continue
            if string in met:
                met[string] += 1
            else:
                met[string] = 1
        max_count = 0
        for key in met:
            if met[key] > max_count:
                max_count = met[key]
        return max_count