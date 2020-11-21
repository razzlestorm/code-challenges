class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        if fast.next is None:
            return slow
        if fast.next is not None and fast.next.next is None:
            return slow.next
