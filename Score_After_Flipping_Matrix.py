class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] = 1 - A[i][j]
        for i in range(n -1):
            count = 0
            for j in range(m):
                count += A[j][i+1]
            if count < m / 2:
                for j in range(m):
                    A[j][i+1] = 1 - A[j][i+1]
        points = 0
        for i in range(m):
            for j in range(n):
                points += 2**(n-j-1) * A[i][j]
        return points