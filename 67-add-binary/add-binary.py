class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ""
        n = len(a) - 1
        m = len(b) - 1
        carry = 0

        while (n >= 0 or m >= 0 or carry == 1):
            digit1 = 0
            digit2 = 0
            
            if (n >= 0):
                digit1 = int(a[n]) 
                n -= 1
            if (m >= 0):
                digit2 = int(b[m]) 
                m -= 1

            total = digit1 + digit2 + carry
            ans += str(total % 2)
            carry = total // 2

        return ans[::-1]



