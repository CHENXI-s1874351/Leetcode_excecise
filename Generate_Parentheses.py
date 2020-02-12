class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        status = []
        indices = []
        index = 0
        while index < 2*n:
            if index == 0:
                status.append('(')
                indices.append([1, 0])
                index += 1
            else:
                nums = len(status)
                index += 1
                for i in range(nums):
                    stat = status.pop(0)
                    left, right = indices.pop(0)
                    if left == right and left < n:
                        status.append(stat + '(')
                        indices.append([left+1, right])
                    elif left > right and left < n:
                        status.append(stat + '(')
                        indices.append([left+1, right])
                        status.append(stat + ')')
                        indices.append([left, right+1])
                    elif left > right and left == n:
                        status.append(stat + ')')
                        indices.append([left, right+1])                       
        return status                  