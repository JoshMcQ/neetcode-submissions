# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum #otherwise false 
                #so its true curSum == targetsum or false
            return (dfs(node.left, curSum) or dfs(node.right, curSum)) 
            #left side or right side true so either path
        return dfs(root, 0)