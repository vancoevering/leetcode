# https://leetcode.com/problems/recover-binary-search-tree/?envType=problem-list-v2&envId=binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traversed = inOrderTraverse(root, [])
        # print([x.val for x in traversed])
        
        first_swap = None
        second_swap = None
        prev = traversed.pop(0)
        for x in traversed:
            if x.val <= prev.val:
                if first_swap is None:
                    first_swap = prev
                second_swap = x
            prev = x
        
        # print("First: ", first_swap)
        # print("Second: ", second_swap)
        swap(first_swap, second_swap)

        
def inOrderTraverse(node: Optional[TreeNode], traversed: List[TreeNode]):
    if node is not None:
        inOrderTraverse(node.left, traversed)
        traversed.append(node)
        inOrderTraverse(node.right, traversed)
    return traversed

def swap(first: TreeNode, second: TreeNode):
    temp = first.val
    first.val = second.val
    second.val = temp
