class Solution:
    def prevGreat(self, height, parr):
        min_ele = -1
        for h in height:
            parr.append(min_ele)
            if min_ele < h:
                min_ele = h

    def nextGreat(self, height, narr):
        min_ele = -1
        n = len(height)
        narr[:] = [0] * n
        for i in range(n - 1, 0, -1):
            narr[i] = min_ele
            if min_ele < height[i]:
                min_ele = height[i]

    def calTrap(self, height, parr, narr):
        count = 0
        for i in range(1, len(height) - 1):
            min_ele = min(parr[i], narr[i])
            if min_ele > height[i]:
                count += min_ele - height[i]
        return count

    def trap(self, height):
        arr1 = []
        arr2 = []
        self.prevGreat(height, arr1)
        self.nextGreat(height, arr2)
        return self.calTrap(height, arr1, arr2)