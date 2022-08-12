# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = 0
        cp_head = head
        while cp_head:
            cp_head = cp_head.next
            l += 1
        
        if l == n:
            return head.next
        
        i = 0
        cp_head = head
        while cp_head:
            if l - n == i + 1:
                cp_head.next = cp_head.next.next
            cp_head = cp_head.next
            i += 1
    
        return head