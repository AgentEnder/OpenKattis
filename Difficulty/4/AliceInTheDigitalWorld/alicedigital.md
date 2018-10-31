# Alice in the Digital World
## https://open.kattis.com/problems/alicedigital

After returning from the Wonderland, Alice needs to improve her scientific skills in the current digital world. Alice decides to participate the ACM - ICPC Asia Nha Trang Regional Contest 2016 to evaluate her actual performance. Her most favorite problem in the contest is following.

Given an array of positive integers A=a1,a2,...,an, a subarray Aji of A is a sequence of continuous elements in A, i.e., Aji=ai,ai+1,...,aj (where 1≤i≤j≤ n). The weight of Aji is the sum of all its elements, i.e., ∑jk=iak.

Given an integer m, your task is to find the maximum weight subarray of A that contains only one m as the minimum element. You can assume that A always contains at least one element with value m.

Input
The input consists of several datasets. The first line of the input contains the number of datasets, which is a positive number and is not greater than 20. The following lines describe the datasets.

Each dataset is described by the following lines:

The first line contains two positive integers n,m(n≤105;m≤26);

The second line contains n positive integers, each with value at most 26.

Output
For each dataset, write in one line the found maximum weight.