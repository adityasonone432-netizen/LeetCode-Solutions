# problem : valid palindrome
# problem link : https://leetcode.com/problems/valid-palindrome/
# difficulty : easy
# logic : check if the string is a palindrome by ignoring non-alphanumeric characters and case sensitivity


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True
