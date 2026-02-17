class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r=[0]*(rowIndex+1)
        r[0]=1
        for i in range(1,rowIndex+1):
            for j in range(i,0,-1):
                r[j]=r[j]+r[j-1]
        return r