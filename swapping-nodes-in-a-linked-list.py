# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find the length of the linked list
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        # Find the kth node from the start
        kth_from_start = head
        for _ in range(k-1):
            kth_from_start = kth_from_start.next
        # Find the kth node from the end
        kth_from_end = head
        for _ in range(n-k):
            kth_from_end = kth_from_end.next
        # Swap the values
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val
        return head