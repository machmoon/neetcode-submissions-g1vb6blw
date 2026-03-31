class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        else:
            longest_substring_length = 0

        for i in range(len(s)):
            current_string = s[i]
            if len(current_string) > longest_substring_length:
                longest_substring_length = len(current_string)
            r = i+1
            while r < len(s):
                if s[r] in current_string:
                    break
                
                current_string+=s[r]
                r+=1
                
                if len(current_string) > longest_substring_length:
                    longest_substring_length = len(current_string)
        return longest_substring_length