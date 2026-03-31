class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0

        hashset = set()

        for i in range(len(nums)):
            hashset.add(nums[i])

        conseq = []

        for i in range(len(nums)):
            if nums[i] - 1 not in hashset:
                conseq.append(nums[i])

        for i in range(len(conseq)):
            n = 0
            while conseq[i] + n in hashset:
                
                n += 1
                result = max(result, n)

        return result