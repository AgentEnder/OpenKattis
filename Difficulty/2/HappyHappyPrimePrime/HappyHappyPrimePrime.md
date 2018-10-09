# Happy Happy Prime Prime
## https://open.kattis.com/problems/happyprime

RILEY VASHTEE: [reading from display] Find the next number in the sequence:

313 331 367 ...? What?
THE DOCTOR: 379.

MARTHA JONES: What?

THE DOCTOR: It’s a sequence of happy primes – 379.

MARTHA JONES: Happy what?

THE DOCTOR: Any number that reduces to one when you take the sum of the square of its digits and continue iterating it until it yields 1 is a happy number. Any number that doesn’t, isn’t. A happy prime is both happy and prime.

THE DOCTOR: I dunno, talk about dumbing down. Don’t they teach recreational mathematics anymore?

Excerpted from “Dr. Who,” Episode 42 (2007).

The number 7 is certainly prime. But is it happy?

7499713010→→→→→72=4942+92=9792+72=13012+32=1012+02=1
It is happy :-) As it happens, 7 is the smallest happy prime. Please note that for the purposes of this problem, 1 is not prime.

For this problem you will write a program to determine if a number is a happy prime.

Input
The first line of input contains a single integer P, (1≤P≤10000), which is the number of data sets that follow. Each data set should be processed identically and independently.

Each data set consists of a single line of input. It contains the data set number, K, followed by the happy prime candidate, m, (1≤m≤10000).

Output
For each data set there is a single line of output. The single output line consists of the data set number, K, followed by a single space followed by the candidate, m, followed by a single space, followed by YES or NO, indicating whether m is a happy prime.