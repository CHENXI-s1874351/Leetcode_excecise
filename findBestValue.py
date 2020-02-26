class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if sum(arr) <= target: return max(arr)
        temp = target
        arr.sort()
        for i in range(len(arr)):
            if target / (len(arr)-i) > arr[i]:
                target -= arr[i]
            elif target / (len(arr)-i) == arr[i]:
                return arr[i]
            else:
                index = i
                break
        num1 = target // (len(arr) - index)
        num2 = num1 + 1 
        sum1 = num1 * (len(arr)-index) + sum(arr[:index])
        sum2 = num2 * (len(arr)-index) + sum(arr[:index])
        remain1 = abs(temp - sum1)
        remain2 = abs(temp - sum2)
        if remain1 <= remain2:
            return num1
        else:
            return num2
