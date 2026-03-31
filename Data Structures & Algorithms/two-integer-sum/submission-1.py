class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        entries = {}

        for i in range(len(nums)):
            find = target - nums[i]

            if find in entries:
                return sorted([i, entries[find]])

            if nums[i] not in entries:
                entries[nums[i]] = i