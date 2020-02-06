class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        # 当最后一位不为9时，只需要将最后一个数字加1即可
        if digits[-1] != 9:
            for i in range(len(digits)):
                if i != len(digits) -1:
                    output.append(digits[i])
                else:
                    output.append(digits[i]+1)
        # 当最后一位为9时，需要分情况讨论
        else:
            index = -1
            while digits[index] == 9 and -index != len(digits):
                output.append(0)
                index -= 1
            # 对于类似99，999的数字
            if digits[index] == 9:
                output.append(0)
                output.append(1)
            # 对于类似199，1999的数字
            elif -index == len(digits):
                output.append(digits[index]+1)
            # 对于类似139，12499的数字
            else:
                for i in range(index, -len(digits)-1, -1):
                    if i == index:
                        output.append(digits[i]+1)
                    else:
                        output.append(digits[i])
            output = output[::-1]
        return output
            



