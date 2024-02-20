**Intro**
To run the script, execute the main() function. This function demonstrates the usage of each algorithm on maps of varying sizes: 300x300, 600x600, and 900x900. Maps are read from files named "cave300x300", "cave600x600", and "cave900x900" respectively by using readFromFile() function. Each algorithm is applied to find the shortest path from a specified start point to a goal point on each map.
The function takes as input a 2D list map representing the ASCII map, and two tuples - start and goal, representing the starting and goal points. The rows and cols variables store the number of rows and columns in the map, respectively.
The distances 2D list stores the distance of each node in the map from the starting node. Initially, all distances are set to float('inf'), except for the starting node, which is set to 0.
The while loop continues until the queue is empty. At each iteration, the first node in the queue is removed and its row and column indices are stored in the row and col variables, respectively.
For each of the four neighboring nodes (above, below, to the left, and to the right of the current node), the following checks are made:
0 <= r < rows and 0 <= c < cols ensure that the neighbor is within the bounds of the map.
map[r][c] != '*' ensures that the neighbor is not lava.
distances[r][c] == float('inf') ensures that the neighbor has not been visited before.

**Functions**
shortest_path_bfs(map, start, goal): Implements Breadth-First Search to find the shortest path from the start point to the goal point on the given map. Returns the length of the path.
shortest_path_A_astr(map, start, goal): Implements A* search to find the shortest path from the start point to the goal point on the given map. Returns the length of the path.
greedy(map_layout, start, goal): Implements Greedy Best-First Search to find the shortest path from the start point to the goal point on the given map. Returns the length of the path.

**Output**
The output of each function is the length of the shortest path found from the start point to the goal point. The result is printed for each map size and algorithm.
