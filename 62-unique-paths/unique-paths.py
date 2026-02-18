class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        top = 1
        bottom = 1
        for i in range(m-1):
            top *= (n+m-2-i)
            bottom *= (i+1)
        return top // bottom     