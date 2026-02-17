class Solution:
    def generate(self, numRows):
        arr = []
        for i in range(numRows):
            row = [0] * (i + 1)
            arr.append(row)
            for j in range(i + 1):
                if j == 0 or j == i:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]
        return arr 