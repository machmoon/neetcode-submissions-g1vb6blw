class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram1 = {}
        anagram2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            one = s[i]
            two = t[i]
            anagram1[one] = 1 + anagram1.get(one, 0)
            anagram2[two] = 1 + anagram2.get(two, 0)
        
        if anagram1 == anagram2:
            return True
        return False
        
        
        