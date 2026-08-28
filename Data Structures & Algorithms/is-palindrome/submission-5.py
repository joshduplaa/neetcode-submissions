class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPtr = 0
        rightPtr = len(s)-1
        while leftPtr<=rightPtr:
            if s[leftPtr].isalnum() == False:
                leftPtr += 1
            elif s[rightPtr].isalnum() == False:
                rightPtr -= 1
            elif s[leftPtr].lower() == s[rightPtr].lower():                
                leftPtr += 1
                rightPtr -= 1
            else:
                return False
        
        return True

        
                 
            