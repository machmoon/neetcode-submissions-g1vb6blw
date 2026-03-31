class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        result = [0]*len(nums)
        if len(nums) == 2:
            return [nums[-1],nums[0]]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i]
            suffix[-i-1] = suffix[-i]*nums[-i-1]

        result[0] = suffix[1]
        
        for i in range(1, len(nums)-1):
            result[i] = prefix[i-1]*suffix[i+1]
        result[-1] = prefix[-2]
        return result
