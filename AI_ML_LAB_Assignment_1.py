
from collections import deque

def is_valid_index_in_matrix(x_coordinate, y_coordinate, n):
    return 0 <= x_coordinate < n and 0 <= y_coordinate < n


def get_moves(x_coordinate, y_coordinate, grid):
    point_move = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    for dx, dy in directions:
        new_x_coordinate, new_y_coordinate = x_coordinate + dx, y_coordinate + dy
        if is_valid_index_in_matrix(new_x_coordinate, new_y_coordinate, len(grid)):
            point_move.append((new_x_coordinate, new_y_coordinate))
    return point_move



from collections import deque

def number_of_steps_req_target_bfs(start_grid, target_grid):
    n = len(start_grid)
    visited = set()
    start_index = None

    # Finding the index of the blank space ('B') in the start grid
    for i in range(n):
        for j in range(n):
            if start_grid[i][j] == 'B':
                start_index = (i, j)
                break
        if start_index:
            break

    if start_index is None:
        raise ValueError("Start grid does not contain a blank space ('B').")

    queue = deque([(start_grid, start_index, 0)])  # Including steps count in the queue
    # print(queue)

    while queue:
        current_grid, (blank_x, blank_y), steps = queue.popleft()
        if current_grid == target_grid:
            return steps

        if tuple(map(tuple, current_grid)) in visited:
            continue
        visited.add(tuple(map(tuple, current_grid)))

        possible_moves = get_moves(blank_x, blank_y, current_grid)

        for move_x, move_y in possible_moves:
            new_grid = [row[:] for row in current_grid]
            new_grid[blank_x][blank_y], new_grid[move_x][move_y] = new_grid[move_x][move_y], new_grid[blank_x][blank_y]
            queue.append((new_grid, (move_x, move_y), steps + 1))

    return -1  # Return -1 if target state is not reachable


def number_of_steps_req_target_dfs(start_grid, target_grid):
    n = len(start_grid)
    start_index = None

    # Finding the index of the blank space ('B') in the start grid
    for i in range(n):
        for j in range(n):
            if start_grid[i][j] == 'B':
                start_index = (i, j)
                break
        if start_index:
            break

    if start_index is None:
        raise ValueError("Start grid does not contain a blank space ('B').")

    stack = deque([(start_grid, start_index, 0)])  # Including steps count in the stack
    visited = set()

    while stack:
        current_grid, (blank_x, blank_y), steps = stack.pop()
        if current_grid == target_grid:
            return steps

        if tuple(map(tuple, current_grid)) in visited:
            continue
        visited.add(tuple(map(tuple, current_grid)))

        possible_moves = get_moves(blank_x, blank_y, current_grid)
        for move_x, move_y in possible_moves:
            new_grid = [row[:] for row in current_grid]
            new_grid[blank_x][blank_y], new_grid[move_x][move_y] = new_grid[move_x][move_y], new_grid[blank_x][blank_y]
            stack.append((new_grid, (move_x, move_y), steps + 1))

    return -1  # Return -1 if target state is not reachable

# Example usage
start_grid = [
    ['3', '2', '1'],
    ['4', '5', '6'],
    ['8', '7', 'B']
]

target_grid = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', 'B']
]

steps_bfs = number_of_steps_req_target_bfs(start_grid, target_grid)
if steps_bfs != -1:
    print("Number of steps required to reach the target grid using BFS:", steps_bfs)
else:
    print("Target state not reachable from the start grid Using BFS.")


steps_dfs = number_of_steps_req_target_dfs(start_grid, target_grid)
if steps_bfs != -1:
    print("Number of steps required to reach the target grid using DFS:", steps_dfs)
else:
    print("Target state not reachable from the start grid Using DFS.")

print("Execution Completed ")

