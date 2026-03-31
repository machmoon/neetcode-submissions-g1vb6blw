class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights)-1
        # while l < len(heights):

        while l<r:
            height = min(heights[l], heights[r])
            result = max(height * (r-l), result)
            
            if heights[l] < heights[r]: l+=1
            else: r-=1

            # l+=1

        return result