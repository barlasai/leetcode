class Solution(object):
    def removeDuplicateLetters(self, s):
        d = {} #O(26)
        for c in s:
            d[c]=d.get(c, 0)+1
        stack = [] #O(26)
        taken = set() #O(26)
        for c in s:
            if c in taken:
                d[c]-=1
                continue
            while stack and stack[-1]>c and d[stack[-1]]:
               t= stack.pop()
               taken.remove(t)
            stack.append(c)
            taken.add(c)
            d[c]-=1
        return "".join(stack)