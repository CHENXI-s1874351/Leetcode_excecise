class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        p = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + mat[i-1][j-1]
        maxLenth = 0
        for i in range(m):
            for j in range(n):
                # 如果i+maxLength已经等于m或者j+maxLenth已经等于n，那从这个元素开始，算出来的count一定小于等于maxlength
                if i+maxLenth < m and j+maxLenth < n and mat[i][j] <= threshold:
                    count = maxLenth
                    left = j
                    up = i
                    right = j + maxLenth
                    down = i + maxLenth
                    sum_ = p[down][right] - p[up][right] - p[down][left] + p[up][left]
                    while down < m and right < n and sum_ <= threshold:
                        down += 1
                        right += 1
                        sum_ = p[down][right] - p[up][right] - p[down][left] + p[up][left]
                        count += 1
                    if sum_ > threshold:
                        count -= 1
                    maxLenth = max(maxLenth, count)
        return maxLenth

