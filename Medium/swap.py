# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = (0, head)
        curr = head

        while curr and curr.next:
            next_pointer = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = next_pointer
            prev.next = second

            prev = curr
            curr = next_pointer

        return dummy.next
