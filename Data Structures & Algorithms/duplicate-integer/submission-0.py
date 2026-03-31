class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = {}

        for i in range(len(nums)):
            if not num.get(nums[i]):
                num[nums[i]] = 1
            else:
                return True
        return False