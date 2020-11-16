# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # This mutates list
        if head is not None:
            cur = head
            while cur:
                if cur.val == 'checked':
                    return True
                else:
                    cur.val = 'checked'
                cur = cur.next
            return False
