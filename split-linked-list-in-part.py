from typing import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # get the length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # get the length of each part
        part_length = length // k
        remainder = length % k
        
        # create the result list
        result = []
        curr = head
        for i in range(k):
            # get the length of the current part
            curr_length = part_length
            if remainder > 0:
                curr_length += 1
                remainder -= 1
            
            # create the current part
            result.append(curr)
            for j in range(curr_length - 1):
                curr = curr.next
            if curr:
                temp = curr.next
                curr.next = None
                curr = temp
        
        return result