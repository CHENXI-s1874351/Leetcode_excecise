class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        equal_list = []
        while len(dominoes) > 0:
            count = 1
            a = dominoes.pop(0)
            pop_list= []
            for i in range(len(dominoes)):
                if (a[0] == dominoes[i][0] and a[1] == dominoes[i][1]) or \
                (a[0] == dominoes[i][1] and a[1] == dominoes[i][0]):
                    count += 1
                    pop_list.append(i)
            # 这边的[::-1]很关键，不然会出现pop out of index错误
            for i in pop_list[::-1]:
                dominoes.pop(i)
            equal_list.append(count)
        equal_num = 0
        for i in equal_list:
            num = i * (i-1) //2
            equal_num += num
        return equal_num
