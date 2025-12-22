class Solution(object):
    def letterCombinations(self, digits):
        b = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        return [] if digits == "" else [ "".join(x) for x in itertools.product(*(b[d] for d in digits if d in b))]