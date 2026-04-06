class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            node, left, right = stack.pop()

            if not (left < node.val < right):
                return False

            if node.right:
                stack.append((node.right, node.val, right))
            if node.left:
                stack.append((node.left, left, node.val))

        return True