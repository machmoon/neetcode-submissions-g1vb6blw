class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bmap = {"[": "]", "(":")", "{":"}"}

        for i in range(len(s)):
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                stack.append(s[i])
            elif not stack or bmap[stack[-1]] != s[i]:
                return False
            else:
                stack.pop()
                
        if not stack:
            return True
        else:
            return False
