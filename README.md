##### LabReport
📄 Overview
This project implements a Depth-First Search (DFS) algorithm to find a path in a randomly generated N×N grid (where N is between 4 and 7). The grid consists of walkable (0) and blocked (1) cells, with randomly assigned start (S) and goal (G) positions.

🧠 Problem Solving Approach:
Grid Initialization:
Generated a random grid with obstacles (1s) and open paths (0s).
Ensured both the start and goal positions were on walkable cells.
DFS Algorithm Implementation:
Used a stack for DFS traversal, with a visited set to avoid revisits.
Maintained a parent dictionary to reconstruct the path from the goal to the start.
Path Reconstruction:

Backtracked using the parent dictionary to build the final DFS path.
Displayed the DFS path and the topological order of node traversal.
Handling Edge Cases:

Managed scenarios with no possible path or fully blocked grids.
Output:
Displays the grid with S and G, the DFS path, and the topological order of node traversal.
Provides "No path found" if the goal is unreachable.
Summary:
The implemented solution efficiently visualizes the grid, performs DFS, and handles edge cases. While DFS does not guarantee the shortest path, it effectively explores all possible routes, showcasing its utility in pathfinding scenarios.
