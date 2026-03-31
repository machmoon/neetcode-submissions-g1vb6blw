class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:

            wordhash = [0] * 26
            
            for char in word:
                index = ord(char)-ord("a")
                wordhash[index] += 1
            
            result[tuple(wordhash)].append(word)

        print(result.values())
        return list(result.values())
                
                

        # solution = []
        # for word in strs:
        #     solution.append(sorted(word))
            
        # for word in strs:

        # ans = []
        # tempstrs = []
        # for str1 in strs:
        #     tempstrs.append(sorted(str1))

        # for i in range(len(tempstrs)):
        #     if tempstrs[i] not in ans:
        #         ans.append(strs[i])
        #     else:
        #         ans[tempstrs[i].index(ans)].append(strs[i])

        # return ans

        #     hashmaps = {}
        #     for j in range(strs[i]):
        #         hashmaps[strs[i][j]] = hashmaps.count(strs[i][j]) + 1
        #         hashmaps[strs[i]] = 
            

        # if dict not in dicts:
        #     create a dict
        #     append to ans


        # else:
        #     dict
        #     append to anagram in ans

