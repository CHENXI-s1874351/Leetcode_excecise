class Solution:
    def add(self, a: int, b: int) -> int:      
        yihuo = (a ^ b) & 0xFFFFFFFF
        jinwei = ((a & b) << 1) & 0xFFFFFFFF
        while jinwei != 0:
            temp1 = (yihuo ^ jinwei) & 0xFFFFFFFF
            temp2 = ((yihuo & jinwei) << 1) & 0xFFFFFFFF
            yihuo = temp1
            jinwei = temp2
        return yihuo if yihuo <= 0x7FFFFFFF else ~(yihuo ^ 0xFFFFFFFF)