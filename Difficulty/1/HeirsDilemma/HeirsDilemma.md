# Heir's Dilemma
## https://open.kattis.com/problems/heirsdilemma
Your favorite uncle has passed away, leaving you a large estate. Bank account numbers, locations of safe deposit boxes, and GPS coordinates to buried treasures are all locked in an electronic safe in your uncle’s office behind a picture of dogs playing poker. One day he showed you the safe with its 9 digit keypad (digits 1 through 9). He told you he wasn’t worried about anyone breaking into his safe because it’s equipped with a self-destruct mechanism that will destroy the contents if anyone attempts a forced entry.

The combination is a sequence of six decimal digits. If an incorrect combination is entered the safe enforces a thirty-second delay before accepting another combination. So a brute-force effort to try all six-digit combinations could take months.

Your uncle had planned to give you, his sole heir, the combination one day, but due to an unfortunate hang-gliding accident in Kansas, you now must rely on your deductive and programming skills to access the key to your inheritance.

Here’s what you know:

The combination c is a sequence of six non-zero decimal digits.

Your mother recalls that she heard your uncle mention that all the digits are different.

You remember that your uncle once said that the six digit number was divisible by each of its individual digits.

An example satisfying these conditions is 123864: all six digits differ, and you can check that 123864 is divisible by each of 1, 2, 3, 8, 6 and 4.

Even with the helpful data, it could take a while to get to open the safe, so the task is likely to be split into several sessions with separate ranges being tested. How many combinations are there to try in the range given?

Input
The input is a line with two space-separated integers L and H, where 123456≤L<H≤987654

Output
Print one integer, the total number of possible combinations to the safe, where each combination c must satisfy the three constraints above, and lie in the range L≤c≤H.