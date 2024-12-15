from typing import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #Write a function to delete a node ina  singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
        node.val = node.next.val
        node.next = node.next.next
        return
        