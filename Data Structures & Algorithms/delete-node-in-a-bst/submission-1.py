# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def minValueNode(root):
            cur = root
            while cur and cur.left:
                cur = cur.left
            return cur

        def remove(node, val):
            if not node:
                return
            if val > node.val:
                node.right = remove(node.right, val)
            elif val < node.val:
                node.left = remove(node.left, val)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    minNode = minValueNode(node.right)
                    node.val = minNode.val
                    node.right = remove(node.right, minNode.val)
            return node

        return remove(root, key)