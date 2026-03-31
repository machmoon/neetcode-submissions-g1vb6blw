class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_array = defaultdict(int)
        s2_window = defaultdict(int)

        for i in range(len(s1)):
            s1_array[s1[i]] += 1
            s2_window[s2[i]] += 1 

        l = 0
        r = len(s1)-1
        
        while r < len(s2):
            if s2_window == s1_array:
                return True

            s2_window[s2[l]] -= 1 
            if s2_window[s2[l]] == 0:
                s2_window.pop(s2[l])
            r+=1
            l+=1
            if r != len(s2):
                s2_window[s2[r]] += 1




        return False



