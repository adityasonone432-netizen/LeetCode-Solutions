# Problem name : 27. Remove Element
# problem link : https://leetcode.com/problems/remove-element/
# Difficulty : Easy
# Logic : Use a while loop to iterate through the array. If the current element is equal to the value to be removed, pop it from the array. Otherwise, move to the next element. Finally, return the length of the modified array.


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
