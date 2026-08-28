class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]":"[","}":"{",")":"("}
        stack = []

        for c in s:
            if c=="[" or c=="{" or c=="(":
                stack.append(c)
            elif c=="]" or c=="}" or c==")":
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
