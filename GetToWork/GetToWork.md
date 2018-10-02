# Get to Work #
## https://open.kattis.com/problems/gettowork ##

You work for a company that has E employees working in town T. There are N towns in the area where the employees live. You want to ensure that everyone will be able to make it to work. Some of the employees are drivers and can drive P passengers. A capacity of P=1 indicates that the driver can only transport themselves to work. You want to ensure that everyone will be able to make it to work and you would like to minimize the number of cars on the road.

You want to calculate the number of cars on the road, with these requirements:

Every employee can get to town T.

The only way an employee may travel between towns is in a car belonging to an employee.

Employees can only take rides from other employees that live in the same town.

The minimum number of cars is used.

Find whether it is possible for everyone to make it to work, and if it is, how many cars will end up driving to the office.

Input
One line containing an integer C,C≤100, the number of test cases in the input file.

For each test case there will be:

One line containing the integer N, the number of towns in your area and the integer T, the town where the office is located.

One line containing the integer E,1≤E≤500, the number of employees.

E lines, one for each employee, each containing:

An integer 1≤H≤N, the home town of the employee, followed by

An integer 0≤P≤6, the number of passengers they can drive. If the employee is not licensed to drive the number will be 0.

You may assume that 1≤T≤N,1≤N≤100.

Output
C lines, one for each test case in the order they occur in the input file, each containing the string “Case #X: ” where X is the number of the test case, starting from 1, followed by:

The string “IMPOSSIBLE”, if there are not enough drivers for everyone to commute; or

N space-separated integers, one for each town from 1 to N, which indicate the number of vehicles commuting from the town.
