# https://leetcode.com/problems/symmetric-tree/?envType=problem-list-v2&envId=binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        # return is_symmetric_rec(root.left, root.right)
        return is_symmetric_iter(root.left, root.right)


def is_symmetric_rec(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    if left is None or right is None:
        return left is right
    
    return (
        (left.val == right.val)
        and is_symmetric_rec(left.left, right.right)
        and is_symmetric_rec(left.right, right.left)
    )

from collections import deque

def is_symmetric_iter(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    l_stack = deque([left])
    r_stack = deque([right])

    while l_stack and r_stack:
        l_curr = l_stack.popleft()
        r_curr = r_stack.popleft()

        if l_curr is None or r_curr is None:
            if not (l_curr is r_curr):
                return False
            continue

        if l_curr.val != r_curr.val:
            return False
        
        l_stack.append(l_curr.left)
        l_stack.append(l_curr.right)

        r_stack.append(r_curr.right)
        r_stack.append(r_curr.left)
    
    return not (l_stack or r_stack)
