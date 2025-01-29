class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)-1):
            a = ord(s[i])
            b = ord(s[i+1])
            dif = a-b
            ad = abs(dif)
            sum += ad
        return sum