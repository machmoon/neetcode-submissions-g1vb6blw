class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height)-1
        leftmax, rightmax = height[l], height[r]
        while l < r:

            
            if leftmax >= rightmax:
                r-=1
                rightmax = max(rightmax, height[r])
                
                result += rightmax - height[r]
            else:
                l+=1
                leftmax = max(leftmax, height[l])
                
                result += leftmax - height[l]
            
            
                

        return result

"""
#
#   #   #
# ### ###   #
#############
0123456789012

find next tallest then l = tallest index r=l+1 take min of r and l
keep a tallest sum and tallest index and running sum
l+=1

fails if l is smaller than right
"""