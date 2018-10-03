# 4 thought
## https://open.kattis.com/problems/4thought
Write a program which, given an integer n as input, will produce a mathematical expression whose solution is n. The solution is restricted to using exactly four 4’s and exactly three of the binary operations selected from the set {∗,+,−,/}. The number 4 is the ONLY number you can use. You are not allowed to concatenate fours to generate other numbers, such as 44 or 444.

For example given n=0, a solution is 4∗4−4∗4=0. Given n=7, a solution is 4+4−4 / 4=7. Division is considered truncating integer division, so that 1/4 is 0 (instead of 0.25). Assume the usual precedence of operations so that 4+4∗4=20, not 32. Not all integer inputs have solutions using four 4’s with the aforementioned restrictions (consider n=11).

Hint: Using your forehead and some forethought should make an answer forthcoming. When in doubt use the fourth.

Input
Input begins with an integer 1≤m≤1000, indicating the number of test cases that follow. Each of the next m lines contain exactly one integer value for n in the range −1000000≤n≤1000000.

Output
For each test case print one line of output containing either an equation using four 4’s to reach the target number or the phrase no solution. Print the equation following the format of the sample output; use spaces to separate the numbers and symbols printed. If there is more than one such equation which evaluates to the target integer, print any one of them.