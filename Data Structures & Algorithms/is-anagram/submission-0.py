class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ScharacterCount = {}
        TcharacterCount = {}

        for item in s:
            ScharacterCount[item] = ScharacterCount.get(item, 0) + 1  # increment count

        for item in t:
            TcharacterCount[item] = TcharacterCount.get(item, 0) + 1  # increment count

        return ScharacterCount == TcharacterCount