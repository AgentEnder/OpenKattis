# Railroad Map
## https://open.kattis.com/problems/railroad

The Slovak national railroad company has recently built new tracks. They want to update their railroad map according to these changes. But they want the map to be as simple as possible. So they decided to remove from the map all the stations that have exactly two other direct connections to other stations (i.e., a single railroad passing through the station).

You will be given the complete map of Slovak railroads. It consists of railway stations numbered from 1 to N, and railroad segments between some pairs of these stations. For each railroad segment we are given its length. Your task is to remove all such stations that are directly connected with exactly two other stations, and output the new map. The new map must contain correct distances between the remaining stations.

Input
The first line of the input file contains an integer T≤10 specifying the number of test cases. Each test case is preceded by a blank line.

Each test case begins with a line with two integers N and M, 1≤N≤10000,1≤M≤30000. The number N denotes the number of stations and M is the number of railroad segments. M lines follow, each with 3 integers a,b, and c (1≤a,b≤N) specifying that there is a railroad segment of length c connecting stations a and b.

You can assume that in each test case there is a path between every two stations. Also, there will always be at least 2 stations that are not directly connected to exactly two other stations.

Output
For each test case, the output shall consist of multiple lines. The first line shall contain a positive integer K – the number of railroads on the simplified map. Each of the next K lines shall contain three integers a,b, and c stating that there is a railroad of length c between stations a and b on the simplified map.

Print a blank line between outputs for different test cases.