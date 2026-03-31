class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l = 0
        while l < len(heights):
            r = len(heights)-1
            while l<r:
                height = min(heights[l], heights[r])
                result = max(height * (r-l), result)
                r-=1

            l+=1

        return result