class Solution:
    def grayCode(self, n: int) -> List[int]:
        arr = []
        arr.append(0)
        for i in range(1,n+1):
            prevLength = len(arr)
            mask = 1 << (i-1)
            for j in range(prevLength, 0, -1):
                arr.append(mask + arr[j-1])
        return arr