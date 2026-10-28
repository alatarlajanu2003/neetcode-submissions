# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepthHelper(self, root, count):
        if not root:
            return count
        left_count = self.maxDepthHelper(root.left, count + 1)
        right_count = self.maxDepthHelper(root.right, count + 1)
        return max(left_count, right_count)
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepthHelper(root.left, 0), self.maxDepthHelper(root.right, 0))