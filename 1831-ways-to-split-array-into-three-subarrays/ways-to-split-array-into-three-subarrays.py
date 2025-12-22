class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        totalSum = sum(nums)        
        firstRangeSum = nums[0]
        
        smallestIndxForEndOfSecond = 1
        smallestSecondRangeSum = nums[1]
        while True:
            if smallestSecondRangeSum >= firstRangeSum:
                break
            smallestIndxForEndOfSecond += 1
            if smallestIndxForEndOfSecond == len(nums) - 1:
                return 0
            smallestSecondRangeSum += nums[smallestIndxForEndOfSecond]
        
        biggestIndxForEndOfSecond = len(nums) - 2
        biggestSecondRangeSum = totalSum - nums[0] - nums[-1]
        while True:
            if totalSum - firstRangeSum - biggestSecondRangeSum >= biggestSecondRangeSum:
                break
            biggestSecondRangeSum -= nums[biggestIndxForEndOfSecond]                
            biggestIndxForEndOfSecond -= 1
            if biggestIndxForEndOfSecond == 0:
                return 0
        
        
        res += ((biggestIndxForEndOfSecond - smallestIndxForEndOfSecond) + 1)
        
        for firstRangeEnd in xrange(1, len(nums) - 2):
            firstRangeSum += nums[firstRangeEnd]
            smallestSecondRangeSum -= nums[firstRangeEnd]
            while True:
                if smallestSecondRangeSum >= firstRangeSum:
                    if smallestIndxForEndOfSecond == firstRangeEnd:
                        smallestIndxForEndOfSecond += 1
                    break
                smallestIndxForEndOfSecond += 1                    
                if smallestIndxForEndOfSecond == len(nums) - 1:
                    return res % (10 ** 9 + 7)
                smallestSecondRangeSum += nums[smallestIndxForEndOfSecond] 
            

            biggestSecondRangeSum -= nums[firstRangeEnd]
            while (biggestIndxForEndOfSecond < len(nums) - 2) and (biggestSecondRangeSum + nums[biggestIndxForEndOfSecond + 1]) <= totalSum - firstRangeSum - (biggestSecondRangeSum + nums[biggestIndxForEndOfSecond + 1]):
                biggestIndxForEndOfSecond += 1
                biggestSecondRangeSum += nums[biggestIndxForEndOfSecond]
            if biggestIndxForEndOfSecond == firstRangeEnd:
                return res % (10 ** 9 + 7)
            
            if biggestIndxForEndOfSecond >= smallestIndxForEndOfSecond:
                res += ((biggestIndxForEndOfSecond - smallestIndxForEndOfSecond) + 1)
        
        return res % (10 ** 9 + 7)
            

                    
            
        
            

            
        
        
        
        
        

            
        
                    
        
        
        
        
        