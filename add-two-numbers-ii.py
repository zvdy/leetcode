# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_num(l):
            num = 0
            while l:
                num = num * 10 + l.val
                l = l.next
            return num
        def get_list(num):
            if num == 0:
                return ListNode(0)
            head = None
            while num:
                head = ListNode(num % 10, head)
                num //= 10
            return head
        return get_list(get_num(l1) + get_num(l2))