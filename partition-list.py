from typing import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]: 
            if head is None:
                return head
            
            left = ListNode()
            right = ListNode()
            
            left_head = left
            right_head = right
            
            while head:
                if head.val < x:
                    left.next = head
                    left = left.next
                else:
                    right.next = head
                    right = right.next
                head = head.next
            
            right.next = None
            left.next = right_head.next
            
            return left_head.next