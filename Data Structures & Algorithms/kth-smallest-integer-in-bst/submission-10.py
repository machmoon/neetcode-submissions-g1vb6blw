# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # dfs 
        stack = []
        stack.append(root)
        curr = stack.pop()

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            
            k-=1
            if k == 0:
                return curr.val

            curr = curr.right

"""
      12
    10 14
   9 
 7  9.5
3
"""