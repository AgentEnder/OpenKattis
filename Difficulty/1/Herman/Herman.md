# Herman
## https://open.kattis.com/problems/herman

The 19th century German mathematician Hermann Minkowski investigated a non-Euclidian geometry, called the taxicab geometry. In taxicab geometry the distance between two points T1(x1,y1) and T2(x2,y2) is defined as:

D(T1,T2)=|x1−x2|+|y1−y2|
All other definitions are the same as in Euclidian geometry, including that of a circle:

A circle is the set of all points in a plane at a fixed distance (the radius) from a fixed point (the centre of the circle).

We are interested in the difference of the areas of two circles with radius R, one of which is in normal (Euclidian) geometry, and the other in taxicab geometry. The burden of solving this difficult problem has fallen onto you.

Input
The first and only line of input will contain the radius R, a positive integer smaller than or equal to 10000.

Output
On the first line you should output the area of a circle with radius R in normal (Euclidian) geometry. On the second line you should output the area of a circle with radius R in taxicab geometry.

Note: Outputs within ±0.0001 of the official solution will be accepted.