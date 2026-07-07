# problem name : Roman to Integer
# problem link : https://leetcode.com/problems/roman-to-integer/
# Difficulty : Easy
# logic : Create a dictionary to map Roman numerals to their integer values. Iterate through the string, and for each character, check if the next character represents a larger value. If it does, subtract the current value from the total; otherwise, add it to the total.


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total
