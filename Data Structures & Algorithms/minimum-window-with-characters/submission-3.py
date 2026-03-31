class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""

        result = [-1,-1]
        result_length = float("inf")

        hashmap = {}
        for i in range(len(t)):
            hashmap[t[i]] = hashmap.get(t[i], 0) + 1
        # char = set(count, index)
        l, r = 0, 0

        window_hashmap = {}

        have, need = 0, len(hashmap)
        while r < len(s):

            window_hashmap[s[r]] = window_hashmap.get(s[r], 0) + 1

            if s[r] in hashmap and hashmap[s[r]] == window_hashmap[s[r]]:
                have += 1

            while need == have:
                if (r-l + 1) < result_length:
                    result = [l, r]
                    result_length = r-l+1

                window_hashmap[s[l]] -= 1

                if s[l] in hashmap and window_hashmap[s[l]] < hashmap[s[l]]:
                    have -= 1
                l += 1

                
            r += 1

        l, r = result
        print(l ,r)

        return s[l: r+1] if result_length != float("inf") else ""
                

        
        # for sliding window check for current s[i] in set if it is then thats the start and then countinue window until all t in the window and if theres a duplicate move left window to first occourance of the next thin in the set
        # sliding window (hashset check if window in it)