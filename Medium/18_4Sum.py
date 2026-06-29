# problem 18: 4Sum
# problem link : https://leetcode.com/problems/4sum/
# Difficulty : Medium
# logic : Sort the array and use two nested loops to fix the first two numbers, then use a two-pointer approach to find the remaining two numbers that sum up to the target. Handle duplicates by skipping over them.


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, n - 1

                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        return ans
