class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        top_sum = - float("inf")
        running_sum = 0

        for i in range(len(nums)):
            running_sum += nums[i]

            if nums[i] > running_sum:
                running_sum = nums[i]
            
            if top_sum < running_sum:
                top_sum = running_sum

        return top_sum
