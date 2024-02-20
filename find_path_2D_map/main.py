from collections import deque
from queue import PriorityQueue
import heapq

def main():
    smallMap = readFromFile("cave300x300")
    mediumMap = readFromFile("cave600x600")
    largeMap = readFromFile("cave900x900")
    print("BFS 300x300 map: ", shortest_path_bfs(smallMap, (2,2), (295,257)))
    print("BFS 600x600 map: ", shortest_path_bfs(mediumMap, (2,2), (598,595)))
    print("BFS 900x900 map: ", shortest_path_bfs(largeMap, (2,2), (898,895)))
    print("A* 300x300 map: ", shortest_path_A_astr(smallMap, (2,2), (295,257)))
    print("A* 600x600 map: ", shortest_path_A_astr(mediumMap, (2,2), (598,595)))
    print("A* 900x900 map: ", shortest_path_A_astr(largeMap, (2,2), (898,895)))
    print("Greedy 300x300 map: ", greedy(smallMap, (2,2), (295,257)))
    print("Greedy 600x600 map: ", greedy(mediumMap, (2,2), (598,595)))
    print("Greedy 900x900 map: ", greedy(largeMap, (2,2), (898,895)))

def readFromFile(file):
    map_data = []
    with open(file) as f:
        map_data = [l.strip() for l in f.readlines() if len(l)>1]
    return map_data

def shortest_path_bfs(map, start, goal):
    rows, cols = len(map), len(map[0])
    distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    queue = deque([(start[0], start[1])])
    while queue:
        row, col = queue.popleft()

        if (row, col) == goal:
            return distances[row][col] # Return the length of the path
            
        for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if 0 <= r < rows and 0 <= c < cols and map[r][c] != '*' and distances[r][c] == float('inf'):
                distances[r][c] = distances[row][col] + 1
                queue.append((r, c))
    return float('inf')  # Return infinity if no path is found

def shortest_path_A_astr(map, start, goal):
    rows, cols = len(map), len(map[0])
    distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    heap = [(0, start[0], start[1])]
    while heap:
        distance, row, col = heapq.heappop(heap)

        if (row, col) == goal:
            return distance # Return the length of the path

        for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if 0 <= r < rows and 0 <= c < cols and map[r][c] != '*' and distance + 1 < distances[r][c]:
                distances[r][c] = distance + 1
                heapq.heappush(heap, (distances[r][c], r, c))
    return float('inf')  # Return infinity if no path is found

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def is_valid_move(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def greedy(map_layout, start, goal):
    rows = len(map_layout)
    cols = len(map_layout[0])

    distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    distances[start[0]][start[1]] = 0

    queue = deque([start])
    came_from = {}

    while queue:
        row, col = queue.popleft()

        if (row, col) == goal:
            return distances[row][col] # Return the length of the path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_node = (row + dx, col + dy)

            if 0 <= next_node[0] < rows and 0 <= next_node[1] < cols and map_layout[next_node[0]][next_node[1]] != '*' and distances[next_node[0]][next_node[1]] == float('inf'):
                distances[next_node[0]][next_node[1]] = distances[row][col] + 1
                queue.append(next_node)
                came_from[next_node] = (row, col)
    return float('inf') # Return infinity if no path is found


if __name__ == "__main__":
    main()
