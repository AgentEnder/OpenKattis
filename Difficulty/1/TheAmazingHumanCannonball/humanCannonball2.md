# The Amazing Human Cannonball
## https://open.kattis.com/problems/humancannonball2


The amazing human cannonball show is coming to town, and you are asked to double-check their calculations to make sure no one gets injured! The human cannonball is fired from a cannon that is a distance x1 from a vertical wall with a hole through which the cannonball must fly. The lower edge of the hole is at height h1 and the upper edge is at height h2. The initial velocity of the cannonball is given as v0 and you also know the angle θ of the cannon relative to the ground.

Thanks to their innovative suits, human cannonballs can fly without air resistance, and thus their trajectory can be modeled using the following formulas:

x(t)y(t)==v0tcosθv0tsinθ−12gt2
where x(t),y(t) provides the position of a cannon ball at time t that is fired from point (0,0). g is the acceleration due to gravity (g=9.81 m/s2).

Write a program to determine if the human cannonball can make it safely through the hole in the wall. To pass safely, there has to be a vertical safety margin of 1 m both below and above the point where the ball’s trajectory crosses the centerline of the wall.

Input
The input will consist of up to 100 test cases. The first line contains an integer N, denoting the number of test cases that follow. Each test case has 5 parameters: v0 θ x1 h1 h2, separated by spaces. v0 (0<v0≤200) represents the ball’s initial velocity in m/s. θ is an angle given in degrees (0<θ<90), x1 (0<x1<1000) is the distance from the cannon to the wall, h1 and h2 (0<h1<h2<1000) are the heights of the lower and upper edges of the wall. All numbers are floating point numbers.

Output
If the cannon ball can safely make it through the wall, output “Safe”. Otherwise, output “Not Safe”!