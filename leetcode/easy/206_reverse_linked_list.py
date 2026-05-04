# LeetCode #206 - Reverse Linked List
# Approach: Iterative - three pointers (prev, current, next)
# Time: O(n) | Space: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev