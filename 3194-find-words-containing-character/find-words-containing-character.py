class Solution(object):
    def findWordsContaining(self, words, x):
        indices = []
        for char in range (len(words)):
            if x in words[char]:
                indices.append(char)
        return(indices)
        
        