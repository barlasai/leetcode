class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"

        s = self.countAndSay(n - 1)
        sb = []

        count = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                sb.append(str(count))
                sb.append(s[i - 1])
                count = 1
            else:
                count += 1

        sb.append(str(count))
        sb.append(s[-1])

        return ''.join(sb)