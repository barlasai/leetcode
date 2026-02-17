class Solution(object):
    def mySqrt(self, x):
        
        low = 1
        high = x
        p = 1

        if x < 2:
            return x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                p = mid
                low = mid + 1
            else:
                high = mid - 1
        return p