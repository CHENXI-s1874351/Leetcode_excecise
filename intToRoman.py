class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = ''
        # 取名建议还是别用拼音
        # 这里是为了看起来清楚
        qianwei = num // 1000
        num = num % 1000
        if qianwei:
            for i in range(qianwei):
                Roman += 'M'
        baiwei = num // 100
        num = num % 100
        if baiwei:
            if baiwei == 9:
                Roman += 'CM'
            elif baiwei < 9 and baiwei >= 5:
                Roman += 'D'
                for i in range(baiwei-5):
                    Roman += 'C'
            elif baiwei == 4:
                Roman += 'CD'
            else:
                for i in range(baiwei):
                    Roman += 'C'
        shiwei = num // 10
        num = num % 10
        if shiwei:
            if shiwei == 9:
                Roman += 'XC'
            elif shiwei < 9 and shiwei >= 5:
                Roman += 'L'
                for i in range(shiwei-5):
                    Roman += 'X'
            elif shiwei == 4:
                Roman += 'XL'
            else:
                for i in range(shiwei):
                    Roman += 'X'
        if num:
            if num == 9:
                Roman += 'IX'
            elif num < 9 and num >= 5:
                Roman += 'V'
                for i in range(num-5):
                    Roman += 'I'
            elif num == 4:
                Roman += 'IV'
            else:
                for i in range(num):
                    Roman += 'I'
        return Roman