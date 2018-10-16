# Faulty Robot
## https://open.kattis.com/problems/faultyrobot

As part of a CS course, Alice just finished programming her robot to explore a graph having n nodes, labeled 1,2,…,n, and m directed edges. Initially the robot starts at node 1.

While nodes may have several outgoing edges, Alice programmed the robot so that any node may have a forced move to a specific one of its neighbors. For example, it may be that node 5 has outgoing edges to neighbors 1, 4, and 6 but that Alice programs the robot so that if it leaves 5 it must go to neighbor 4.

If operating correctly, the robot will always follow forced moves away from a node, and if reaching a node that does not have a forced move, the robot stops. Unfortunately, the robot is a bit buggy, and it might violate those rules and move to a randomly chosen neighbor of a node (whether or not there had been a designated forced move from that node). However, such a bug will occur at most once (and might never happen).

Alice is having trouble debugging the robot, and would like your help to determine what are the possible nodes where the robot could stop and not move again.

We consider two sample graphs, as given in Figures 1 and 2. In these figures, a red arrow indicate an edge corresponding to a forced move, while black arrows indicate edges to other neighbors. The circle around a node is red if it is a possible stopping node.

![Faulty1](https://open.kattis.com/problems/faultyrobot/file/statement/en/img-0001.png)
Figure 1: First sample graph.
![Faulty2](https://open.kattis.com/problems/faultyrobot/file/statement/en/img-0002.png)
Figure 2: Second sample graph.
In the first example, the robot will cycle forever through nodes 1, 5, and 4 if it does not make a buggy move. A bug could cause it to jump from 1 to 2, but that would be the only buggy move, and so it would never move on from there. It might also jump from 5 to 6 and then have a forced move to end at 7.

In the second example, there are no forced moves, so the robot would stay at 1 without any buggy moves. It might also make a buggy move from 1 to either 2 or 3, after which it would stop.