# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        slow_node = head
        fast_node = head.next
        while fast_node and fast_node.next:
            if fast_node == slow_node:
                return True

            slow_node = slow_node.next
            fast_node = fast_node.next.next

        return False