# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def traverse(self, root, result, level):
        # []
        # [[4,5,6,7], [2,3],[1]]
        if not root:
            return

        if len(result) <= level:
            result.append([root.val])
        else:
            result[level].append(root.val)

        self.traverse(root.left, result, level+1)
        self.traverse(root.right, result, level+1)

        
        
        
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []      

        self.traverse(root, result, 0)

        return result