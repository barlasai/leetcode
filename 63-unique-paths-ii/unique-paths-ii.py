class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]

        def function(r, c):
            if r < 0 or c < 0: return 0
            if obstacleGrid[r][c] == 1: return 0
            if r == 0 and c == 0: return 1
            if dp[r][c] != -1: return dp[r][c]
            
            dp[r][c] = function(r - 1, c) + function(r, c - 1)
            return dp[r][c]

        return function(m - 1, n - 1)