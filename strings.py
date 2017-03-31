# Reverse a string
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        return self.reverseString(s[n/2:]) + self.reverseString(s[:n/2])

        # Can also use
        # return s[::-1]
