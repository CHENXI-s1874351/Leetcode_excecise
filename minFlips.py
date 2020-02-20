class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        str_a = str(bin(a))[2:]
        str_b = str(bin(b))[2:]
        str_c = str(bin(c))[2:]
        str_a = '0'*(32-len(str_a)) + str_a
        str_b = '0'*(32-len(str_b)) + str_b
        str_c = '0'*(32-len(str_c)) + str_c
        count = 0
        for a, b, c in zip(str_a, str_b, str_c):
            if c == '0':
                if a == '1':
                    count += 1
                if b == '1':
                    count += 1
            else:
                if a == '0' and b == '0':
                    count += 1
        return count

        # 当然也可以用单纯的位运算来解决这个问题
        #count = 0
        #while a != 0 or b != 0 or c != 0:
            #a_, b_, c_ = a & 1, b & 1, c & 1
            #if a_ | b_ == c_: 
                #pass
            #else:
                #if c_ == 0:
                    #if a_ == 1: count +=1
                    #if b_ == 1: count += 1
                #else:
                    #count += 1
            #a, b, c = a >> 1, b >> 1, c >> 1
        #return count