class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for s in strs:
            newString = str(len(s)) + "#" + s
            result = result + newString
        
        print(result)
        
        return result
    def decode(self, s: str) -> List[str]:
        words = []
        c = 0
        word_length = ""
        while c < len(s):
            if s[c] == "#":
                word_len = int(word_length)
                new_word = s[c+1:c+word_len+1]
                words.append(new_word)
                c = c+word_len+1
                word_length = ""
            else:
                word_length = word_length + s[c]
                c += 1

        return words

