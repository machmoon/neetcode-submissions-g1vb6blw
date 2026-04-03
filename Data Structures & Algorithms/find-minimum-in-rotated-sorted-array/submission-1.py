class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        result = nums[(l+r)//2]

        while l<=r:
            m = (l+r)//2

            result = min(result, nums[m])

            if nums[l] <= nums[m]:
                if nums[l] <= nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else: 
                if nums[l] >= nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return result