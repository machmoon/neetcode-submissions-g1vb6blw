# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        queue = deque()
        visited = []

        if root != None:
            curr = root

            queue.append(curr)
            
        level = 0
        while queue:
            for i in range(len(queue)):

                curr = queue.popleft()

                if curr.right != None:
                    queue.append(curr.right)

                if curr.left != None:
                    queue.append(curr.left)
            level += 1

        return level
            