class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        n = (numRows-2)*2+1
        arr = [[n+1]]
        j = 1
        while n > 1:
            arr.append([n-1, j+1])
            n -= 2
            j += 2
        arr.append([arr[0][0]])
        output = ''
        for i in range(len(arr)):
            if i == 0:
                interval = arr[i][0]
                j = 0
                while j <= len(s) - 1:
                    output += s[j]
                    j += interval
            elif i == len(arr) - 1:
                interval = arr[i][0]
                j = i
                while j <= len(s) - 1:
                    output += s[j]
                    j += interval 
            else:
                index = 0
                j = i
                while j <= len(s) - 1:
                    output += s[j]
                    j += arr[i][index]
                    index = 1 - index
        return output