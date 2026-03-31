class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0

        hashset = set(nums)


        # conseq = []

        for i in range(len(nums)):
            if nums[i] - 1 not in hashset:
                n = 0
                while nums[i] + n in hashset:
                    
                    n += 1
                    result = max(result, n)
                # conseq.append(nums[i])

        # for i in range(len(conseq)):
            

        return result