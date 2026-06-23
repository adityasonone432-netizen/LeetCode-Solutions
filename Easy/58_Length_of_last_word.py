# problem: Length of Last Word
# problem link : https://leetcode.com/problems/length-of-last-word/
# Difficulty : Easy
# logic : Use the rstrip() method to remove trailing spaces, then split the string into


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        if len(lst) == 0:
            return 0
        return len(lst[-1])
