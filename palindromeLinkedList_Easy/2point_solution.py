# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(node):
            prev_node = None
            while node != None:
                next_node = node.next
                node.next = prev_node
                prev_node = node
                node = next_node
            return prev_node
        fast = head
        slow = head
        # Goes through list until lit reaches end, so slow is the next-to-last value
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        fast = head
        slow = reverse(slow)
        # This then checks against the reversed list
        while slow is not None:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
