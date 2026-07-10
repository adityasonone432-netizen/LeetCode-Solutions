# Problem: Calculate the nth Fibonacci number.
# problem link: https://leetcode.com/problems/fibonacci-number/
# difficulty: Easy
# logic: Dynamic Programming


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a = 0  # f(0)=0
        b = 1  # f(1)=1

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b
