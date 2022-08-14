# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lis_ = []
        while head:
            lis_.append(head.val)
            head = head.next
        
        return lis_ == lis_[::-1]