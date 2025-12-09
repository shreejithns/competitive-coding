from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseLinkedList(start: ListNode, end: ListNode) -> ListNode:
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev  # New head after reversal

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Find the kth node
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Less than k nodes left

            group_next = kth.next  # The node after kth

            # Reverse this group
            prev, curr = kth.next, group_prev.next
            # Reverse from curr to kth
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Connect with previous part
            nxt_group_head = group_prev.next
            group_prev.next = kth
            group_prev = nxt_group_head
