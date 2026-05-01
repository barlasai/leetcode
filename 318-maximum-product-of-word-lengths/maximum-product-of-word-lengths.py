class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        maxx=0
        sets=[set(word) for word in words]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and not sets[i]&sets[j]:
                    maxx=max(maxx,len(words[i])*len(words[j]))
        return maxx
        