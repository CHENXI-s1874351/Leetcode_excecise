class Solution:
    def sumNums(self, n: int) -> int:
        return n + ((n>=1) and self.sumNums(n-1))