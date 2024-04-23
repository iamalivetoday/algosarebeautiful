class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        ret = ""
        #one character at a time into the 
        for i, c in enumerate(word1):
            ret = ret + str(c)
            if i < len(word2):
                ret += word2[i]

        if len(word1) < len(word2):
            remainder = word2[len(word1):]
            ret += remainder
        
        return ret
        