# https://leetcode.com/problems/unique-binary-search-trees/?envType=problem-list-v2&envId=binary-tree
class Solution:
    def numTrees(self, n: int) -> int:
        return numSubtrees(1, n)

# Too slow, so we can cache
from functools import cache

@cache
def numSubtrees(start: int, end: int) -> int:
    total = 0

    if start >= end:
        # two cases:
        # > : one subtree with no children
        # ==: one subtree with one child
        return 1

    # Looping through possible parent root nodes
    # We want the upper bound to be inclusive
    for i in range(start, end+1):
        left_subtrees = numSubtrees(start, i-1)
        right_subtrees = numSubtrees(i+1, end)

        total += left_subtrees * right_subtrees
    
    return total
