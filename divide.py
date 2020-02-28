class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            temp = divisor
            c = 0
            while dividend >= temp:
                temp = temp << 1
                c += 1
            count += 2**(c-1)
            dividend -= (temp >> 1)
        if sign == 1: count = -count
        return count if count >= -2**31 and count <= 2**31-1 else 2**31-1
