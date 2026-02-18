class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0                 # i for s, j for p
        star = -1                 # most recent '*' position in p
        match = 0                 # position in s when we saw that '*'

        while i < len(s):
            # 1) exact match or '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # 2) '*' found: record and move pattern
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1  # assume '*' matches empty first

            # 3) mismatch: try to use previous '*'
            elif star != -1:
                j = star + 1      # reset pattern to after '*'
                match += 1        # let '*' match one more char
                i = match

            # 4) mismatch and no '*' to save us
            else:
                return False

        # consume trailing '*' in pattern
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)