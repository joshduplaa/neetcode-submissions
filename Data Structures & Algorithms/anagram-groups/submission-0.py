class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #an anagram is a string that contains all the characters of another string
        #switch type from strings to set
        groups = {}  # regular dict
        
        for word in strs:
            key = ''.join(sorted(word))  # same sorted key
            if key not in groups:
                groups[key] = []  # manually initialize list
            groups[key].append(word)
        
        return list(groups.values())
            