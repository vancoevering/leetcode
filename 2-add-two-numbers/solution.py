# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = reverse_linked_to_number(l1)
        n2 = reverse_linked_to_number(l2)
        sum = n1 + n2
        return number_to_reverse_linked(sum)


def number_to_reverse_linked(num: int):
    # This is valid so long as num is non-negative
    digits = []
    while True:
        digits.append(num % 10)
        num = num // 10
        if num == 0:
            break
    digits = reversed(digits)

    node = None
    next_node = None
    for d in digits:
        node = ListNode(val=d, next=next_node)
        next_node = node

    return node


def reverse_linked_to_number(node: ListNode):
    num = 0
    power = 0
    while True:
        num += node.val * (10**power)
        if node.next is None:
            return num

        power += 1
        node = node.next
