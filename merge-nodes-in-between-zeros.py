from typing import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None
    if not head.next.val:
      node = ListNode(head.val)
      node.next = self.mergeNodes(head.next.next)
      return node

    next = self.mergeNodes(head.next)
    next.val += head.val
    return next
