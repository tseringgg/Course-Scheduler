# Final Project Documentation
Aaron Borjas, Connor Weldy, Jorjei Ngoche
December 10, 2022
CS473 Advanced Algorithms Design and Analysis, Dr. Kent Jones

Hypothetical:
greedy-bfs-based coloring: O(V^3 + E), w/ v = classes, e = can't go together
degree-based coloring: O(V^3 + VlogV) => O(V^3)

EMPIRICAL SPEEDS (N inputs) (11 time slots, 10 rooms)
Greedy-bfs-based coloring: 0.0000770092 seconds => 77.0 microseconds
degree-based coloring: 0.0000438690 seconds => 43.8 microseconds

SPEEDS (2N inputs) (11 time slots, 10 rooms)
Greedy-bfs-based coloring: 0.0001511574 => 151.1 microseconds
degree-based coloring: 0.0000860691 => 86.07 microseconds

GREEDY EMPIRICAL RATIO:
151.1 microseconds / 77.0 microseconds = 1.96
DEGREE EMPIRICAL RATIO:
86.07 microseconds / 43.8 microseconds = 1.97


HYPOTHETICAL RATIO: 
greedy-bfs-based coloring: O(V+E)
2V+2E / V+E == 2
v = 21, e = 84, 2v = 42, 2e = 152 (2V+2E)/(V+E) = 2

degree-based coloring: Average Case: O(V + VlogV)
(2V + 2Vlog2V)/(V + VlogV) == 2


