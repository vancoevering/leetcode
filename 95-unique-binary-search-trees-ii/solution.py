# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return all_bst_trees(1, n)

import functools

@functools.cache
def all_bst_trees(start: int, end: int) -> List[Optional[TreeNode]]:
    result = []
    
    if start > end:
        result.append(None)
        return result
    
    for i in range(start, end+1):
        left_subtrees = all_bst_trees(start, i-1)
        right_subtrees = all_bst_trees(i+1, end)

        for l in left_subtrees:
            for r in right_subtrees:
                node = TreeNode(i, l, r)
                result.append(node)
    
    
    return result
