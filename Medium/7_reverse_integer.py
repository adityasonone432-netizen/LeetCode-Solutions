# Problem 7 : Reverse Integer
# link : https://leetcode.com/problems/reverse-integer/description/
# Difficulty : Medium
# Logic : Modulo (%) and Integer Division (//) to extract and reverse digits. Handle sign and overflow.


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x != 0:
            digit = x % 10
            res = res * 10 + digit

            x //= 10
        res *= sign

        if res < -(2**31) or res > 2**31 - 1:
            return 0
        return res
