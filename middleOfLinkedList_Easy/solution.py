# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Input is head of a LL
        # Output is a ListNode object
        # check edge case of LL of len(1):

        if head.next is None:
            return head
        # run through the list once, keep track of how long it is
        curr = head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        # run through list until halfway point is reached
        curr = head
        stop = -(-count//2)
        while count > stop:
            count -= 1
            curr = curr.next
        return curr
