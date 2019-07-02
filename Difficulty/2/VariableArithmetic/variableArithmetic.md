# Variable Arithmetic
Computers are great at helping humans perform mathematical operations. A person can define names (aka variables) to represent numbers, and then write statements that have deeper semantic meaning. For example, rather than ‘3 + 8’, one could write ‘length + width’. Assuming the computer knows the correct values of the variables length and width, the computer will arrive at the correct answer.

Write a program that allows a user to define integer variables and enter arithmetic sums. The program should record the variable definitions and re-print simplified versions of the arithmetic sums. A variable definition has the following format: x=y, where x is the variable name, and y is a positive integer. Each variable name is a sequence of lowercase characters. An arithmetic sum is a sequence of variables and positive integers separated by plus signs.

Keep track of variable definitions (and re-definitions) over time, as the user enters them. Each variable definition affects subsequent statements which use that variable.

Simplify the arithmetic statements as much as possible, substituting the values for any variables that have been previously defined. Then print the numeric value of the portion of the statement that can be simplified, if it is non-zero. Then, if any variables referenced in the statement haven’t yet been defined, print those in the order given in the input, with arithmetic operations intact.

Input
Input consists of a sequence of up to 2000 lines, where each line is a variable definition or an arithmetic statement using integers or variables. All variable names use 1 to 15 lowercase letters (a–z), and all numbers are in the range [0,100]. Arithmetic sums contain up to 100 terms, excluding the plus signs. All input tokens are separated by single spaces. The last test case is followed by a line containing only the number 0.

Output
For each arithmetic statement, print a line with the simplified form of that statement, following the guidelines given earlier.