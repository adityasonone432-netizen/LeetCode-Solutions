# problem: Move Zeroes
# problem link: https://leetcode.com/problems/move-zeroes/
# difficulty: easy
# logic : use two pointers to move all the zeroes to the end of the array while maintaining the relative order of the non-zero elements.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
