from typing import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        curr = head
        n = 1
        while curr:
            stack.append(curr.val)
            curr = curr.next
            n += 1
        halfsizeofll = n/2
        curr = head
        sums = []
        index = 1
        while index < halfsizeofll:
            sums.append(curr.val+stack.pop())
            index += 1
            curr = curr.next
        return max(sums)

