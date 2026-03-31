class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        result = 0
        window = {}
        l, r = 0, 0

        while r < len(s):
            # Update counts of char in the window
            window[s[r]] = window.get(s[r], 0) + 1

            # Check if len of window - most frequest char <= k
            # If it is that means maybe new window length
            # If its not decrease count of it and shift window
            if (r-l+1) - max(window.values()) <= k:
                result = max(result, r - l + 1)
            else:
                window[s[l]] = window.get(s[l], 0) - 1
                l+=1

            r += 1

            

        return result