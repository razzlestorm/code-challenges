# Definition for singly-linked list.

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Initial, naive Solution
        forward = []
        reverse = []
        curr = head
        while curr is not None:
            forward.append(curr.val)
            reverse.insert(0, curr.val)
            curr = curr.next
        return True if forward == reverse else False
