# problem : Search Insert Position
# problem link : https://leetcode.com/problems/search-insert-position/
# difficulty : easy
# logic : use binary search to find the position of the target in the sorted array.


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1
        return left
