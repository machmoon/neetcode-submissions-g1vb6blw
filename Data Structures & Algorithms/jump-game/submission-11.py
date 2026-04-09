class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = nums[0]

        for i in range(len(nums)-1):
            if nums[i] > gas:
                gas = nums[i]
            elif gas == 0:
                return False

            gas -= 1

        return True
