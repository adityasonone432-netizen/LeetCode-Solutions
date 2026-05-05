# problem name: 26. Remove Duplicates from Sorted Array
# Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# logic : Use two pointers, one slow and one fast. The fast pointer iterates through the array, while the slow pointer keeps track of the position of the last unique element. When a new unique element is found, it is moved to the position after the last unique element, and the slow pointer is incremented. Finally, return the length of the array with unique elements.


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
