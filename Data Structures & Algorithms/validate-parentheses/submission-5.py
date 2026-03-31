class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        # While stack isnt empty [

        for i in range(len(s)):
            if s[i] in pairs.keys():
                stack.append(s[i])
            
            elif len(stack) != 0 and pairs[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
        
# Input: s = "[(])"

# Output: false