class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""

        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            ans += word1[i]
            i += 1
            ans += word2[j]
            j += 1

        if i < len(word1):
            ans += word1[i:]
        if j < len(word2):
            ans += word2[j:]

        return ans