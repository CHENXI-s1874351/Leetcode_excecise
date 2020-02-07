# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mid = (1 + n) // 2
        left = 1
        right = n
        while guess(mid) != 0:
            if guess(mid) == 1:
                left = mid
                mid = (left + right + 1) // 2
            else:
                right = mid
                mid = (left + right) // 2
        return mid