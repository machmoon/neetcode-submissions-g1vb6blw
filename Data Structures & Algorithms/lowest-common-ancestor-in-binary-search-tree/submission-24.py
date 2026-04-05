# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        result = root
        stack = []

        stack.append(root)

        seen_p = False
        seen_q = False

        while stack:
            print(stack)
            curr = stack.pop()
            if curr:
                print(curr.val)

            if curr.val==p.val or curr.val==q.val:
                return curr

            if p.val < curr.val and q.val < curr.val and curr.left:
                
                result = curr.left
                print(f"you {result.val}")
                stack.append(curr.left)
                continue
                
            elif p.val > curr.val and q.val > curr.val and curr.right:
                result = curr.right
                stack.append(curr.right)
                continue

        return result
#     5
#   3   8
#  1 4 7 9
# 0 2
# 2 and 4