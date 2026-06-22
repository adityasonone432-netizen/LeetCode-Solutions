# problem 8: String to Integer (atoi)
# problem link : https://leetcode.com/problems/string-to-integer-atoi/
# Difficulty : Medium
# logic : Use a pointer to traverse the string, skipping whitespace, handling optional sign, and converting digits to an integer. Handle overflow and invalid input.


class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Handle sign
        sign = 1
        i = 0
        if s[0] in ["-", "+"]:
            if s[0] == "-":
                sign = -1
            i += 1

        # Step 3: Convert digits
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1

        # Step 4: Apply sign
        result *= sign

        # Step 5: Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
