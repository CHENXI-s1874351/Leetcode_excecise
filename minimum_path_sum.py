class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])        
        dp = [[0 for j in range(n)] for i in range(m)]
        
        dp[m-1][n-1] = grid[m-1][n-1]
        
        for i in range(n-1):
            dp[m-1][n-i-2] = dp[m-1][n-i-1] + grid[m-1][n-i-2]
        
        for i in range(m-1):
            
            dp[m-i-2][n-1] = dp[m-i-1][n-1] + grid[m-i-2][n-1]
        
        for i in range(m-1):
            for j in range(n-1):
                dp[m-i-2][n-j-2] = grid[m-i-2][n-j-2] + min(dp[m-i-2][n-j-1], dp[m-i-1][n-j-2])
        
        return dp[0][0]
            
                