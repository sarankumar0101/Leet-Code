class Solution(object):
    def firstPalindrome(self, words):
        for char in words:
            r_words = char[::-1]
            if char == r_words:
                return(char)
        return""