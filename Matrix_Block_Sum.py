class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        p = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + mat[i-1][j-1]
        output = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                up = max(i - K, 0)
                down = min(i + K, m-1)
                left = max(j - K, 0)
                right = min(j + K, n-1)
                output[i][j] = p[down+1][right+1] - p[up][right+1] - p[down+1][left] + p[up][left]
        return output
