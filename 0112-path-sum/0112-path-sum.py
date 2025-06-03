# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def has_sum(root,curr_value):

            if not root:
                return False
            
            curr_value += root.val

            if not root.left and not root.right:
                return curr_value == targetSum

            return has_sum(root.right,curr_value) or has_sum(root.left,curr_value)

        return has_sum(root,0)
        