class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0: return 0
        length = len(str(n))
        arr = []
        for i in range(length-1):
            if i == 0:
                arr.append(1)
            else:
                arr.append(10**i+arr[-1]*10)
        
        def dfs(m):
            length = len(str(m))
            first_digit = m // (10**(length-1))
            if m == 0: return 0
            if m < 10: return 1
            if str(m)[0] == '1':
                remainder = m % (10**(length-1))
                return arr[length-2] + (remainder+1) + dfs(remainder)
            else:
                remainder = m % (10**(length-1))
                return first_digit * arr[length-2] + 10 ** (length-1) + dfs(remainder)
        
        return dfs(n)
