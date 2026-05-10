# problem name : Longest substring without reapiting charcters
# problem link : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty : medium
# Logic : Use a sliding window approach with two pointers (left and right) to track the current substring. Use a set to store characters in the current window. Move the right pointer to expand the window and add characters to the set. If a character is repeated, move the left pointer to shrink the window until the repeated character is removed from the set. Keep track of the maximum length of the substring found.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            current_len = right - left + 1

            max_len = max(max_len, current_len)
        return max_len
