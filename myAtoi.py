class Solution:
    def myAtoi(self, string: str) -> int:
        num_appeared = False
        fuhao = 0
        nums_dict = {}
        for i in range(10):
            nums_dict[str(i)] = i
        nums = []
        for ch in string.lstrip():
            # 当出现如同'123  1'的时候
            if ch == ' ' and num_appeared:
                break
            # 当出现如同'+ 123'的时候
            if ch == ' ' and not num_appeared:
                return 0
            # 处理符号位
            if not num_appeared and ch in '+-':
                # 当出现如同'+-1'的时候
                if fuhao != 0:
                    return 0
                if ch == '+':
                    fuhao = 1
                else:
                    fuhao = -1
            # 处理数字位
            elif ch in nums_dict:
                nums.append(nums_dict[ch])
                if not num_appeared:
                    num_appeared = True
            else:
                # 当非法字符出现在数字之后时
                if num_appeared:
                    break
                # 当非法字符出现在数字之前时，return 0
                else:
                    return 0

        if num_appeared:
            num_without_fuhao = self.computeNum(nums)
            if fuhao == 0 or fuhao == 1:
                return min(2**31-1, num_without_fuhao)
            else:
                return max(-2**31, -1*num_without_fuhao)
        # 空字符串或者字符串全是空格
        else:
            return 0 

    def computeNum(self, nums):
        sum_num = 0
        for i in range(len(nums)):
            sum_num += 10 ** (len(nums)-1-i) * nums[i]
        return sum_num

