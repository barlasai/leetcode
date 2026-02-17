class Solution(object):
    def maxChunksToSorted(self, arr):
        n = len(arr)
        maxOfLeft = [0] * n
        minOfRight = [0] * n

        maxOfLeft[0] = arr[0]
        for i in range(1, n):
            maxOfLeft[i] = max(maxOfLeft[i-1], arr[i])

        minOfRight[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            minOfRight[i] = min(minOfRight[i + 1], arr[i])

        res = 0
        for i in range(n - 1):
            if maxOfLeft[i] <= minOfRight[i + 1]:
                res += 1

        return res + 1