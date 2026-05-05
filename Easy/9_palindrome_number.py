# Problem 9 : Palindrome Number
# link : https://leetcode.com/problems/palindrome-number/description/
# Difficulty : Easy
# Logic : Convert the integer to a string and check if it reads the same forwards and backwards.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)

        return s == s[::-1]
