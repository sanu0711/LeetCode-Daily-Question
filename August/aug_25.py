# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self ,node,result):
        if node is None:
            return
        self.helper(node.left,result)
        self.helper(node.right,result)
        result.append(node.val)
        return result
    def postorderTraversal(self, root) -> list[int]:
        temp = []
        result=self.helper(root,temp)
        return result
        
