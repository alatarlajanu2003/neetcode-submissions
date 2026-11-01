# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root:Optional[TreeNode]) -> int:
        if not root or not(root.left or root.right):
            return 0

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def diameterOfBinaryTreeHelper(curr):
            nonlocal result

            if not curr:
                return 0
            
            left_height = self.getHeight(curr.left)
            right_height = self.getHeight(curr.right)
            print(left_height, right_height)
            
            nr_of_children = 0
            if curr.left and curr.right:
                nr_of_children = 2
            elif curr.left or curr.right:
                nr_of_children = 1                
                
            result = max(result, nr_of_children + left_height + right_height)
            
            diameterOfBinaryTreeHelper(curr.left)
            diameterOfBinaryTreeHelper(curr.right)

        diameterOfBinaryTreeHelper(root)
        return result

        

        
