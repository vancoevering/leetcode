from collections import deque

# https://leetcode.com/problems/validate-binary-search-tree/?envType=problem-list-v2&envId=binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return isValidNode(root, None, None)
        # traversed = inOrderTraverse(root, deque())
        # if len(traversed) == 0:
        #     return True
        
        # print(traversed)
        # previous = traversed.popleft()
        # for x in traversed:
        #     if x <= previous:
        #         return False
        #     previous = x
        
        # return True


# via intuition
def isValidNode(node: Optional[TreeNode], left_of: Optional[int], right_of: Optional[int]) -> bool:
    if node is None:
        return True
    
    value = node.val
    if left_of is not None and value >= left_of:
        return False

    if right_of is not None and value <= right_of:
        return False
    
    return isValidNode(node.left, left_of=value, right_of=right_of) and isValidNode(node.right, left_of=left_of, right_of=value)

# Using the BST definition
def inOrderTraverse(node: Optional[TreeNode], traversed: deque[int]):
    if node is not None:
        inOrderTraverse(node.left, traversed)
        traversed.append(node.val)
        inOrderTraverse(node.right, traversed)
    return traversed
