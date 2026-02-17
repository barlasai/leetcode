class Solution(object):
    def maxSubArray(self, nums):
        maxsum = float('-inf')
        midsum = 0
        for num in nums:
            midsum += num
            
            if num > midsum:
                midsum = num
            
            if midsum > maxsum:
                maxsum = midsum
        return maxsum