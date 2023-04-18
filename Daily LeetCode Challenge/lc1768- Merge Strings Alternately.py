class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        @LC1768 - Merge Strings Alternately
        flipped = False
        if len(word1)>len(word2):
            word2,word1 = word1,word2
            flipped = True

        i=0
        j = len(word1)-1

        res =""

        while i<=j:
            if not flipped:
                res+=word1[i]
                res+=word2[i]
            else:
                res+=word2[i]
                res+=word1[i]

            i+=1

        if i <= len(word2):
            res+= word2[i:]

        return res
