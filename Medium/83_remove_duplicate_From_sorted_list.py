# problem 83: Remove Duplicates from Sorted List
# problem link : https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty : Easy
# logic : Iterate through the linked list and remove duplicates by adjusting the next pointers.


class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:

            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
