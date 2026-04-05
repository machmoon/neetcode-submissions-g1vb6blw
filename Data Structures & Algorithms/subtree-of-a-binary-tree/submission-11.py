# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack = []

        if subRoot is None and root is None:
            return True

        if root != None:
            stack.append(root)

        while stack:
            
            curr = stack.pop()
            print(curr.val, subRoot.val)

            if curr.val == subRoot.val:
                if self.isSameTree(curr, subRoot):
                    # print(root, subRoot)
                    return True
            
            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)

        return False

            


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
                return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
        return False

