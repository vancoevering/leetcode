# https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=problem-list-v2&envId=binary-tree&
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        Solution.traverse(root, result)
        return result
    
    @staticmethod
    def traverse(node: Optional[TreeNode], traversed: List[int]):
        # Modifies `traversed` in-place
        if node is not None:
            Solution.traverse(node.left, traversed)
            traversed.append(node.val)
            Solution.traverse(node.right, traversed)
