class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = map(str, xrange(1,10))
        perm = ''
        k , factorial = k-1, 1
        for i in xrange(1, n):
            factorial *= i

        for i in xrange(n):
            index = k / factorial
            k = k % factorial
            factorial = factorial / (n-1-i) if n-1-i else 1
            perm += nums[index]
            del nums[index]
        return perm 