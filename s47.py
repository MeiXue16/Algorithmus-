class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp= [[0 for j in range(n+1)] for i in range (m+1)] # m+1行， n+1列
        #dp = [ [0]*(n+1) for i in range(m+1)] # m+1行， n+1列
        #扩容一行一列，这样不用考虑边界
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = max( dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1] 
        return dp[m][n]

    
    # method 2:
 class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n): # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m): # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]


   
