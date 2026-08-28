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
        if not stack:
            return True
        else:
            return False
