def count_islands(grid):
    def dfs_iterative(x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if cx < 0 or cy < 0 or cx >= n or cy >= m or grid[cx][cy] == '0':
                continue
            grid[cx][cy] = '0'  # Mark the cell as visited
            # Push all neighbors onto the stack
            stack.append((cx + 1, cy))
            stack.append((cx - 1, cy))
            stack.append((cx, cy + 1))
            stack.append((cx, cy - 1))

    n = len(grid)
    m = len(grid[0])
    islands = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':  # Found an unvisited land cell
                islands += 1
                dfs_iterative(i, j)  # Perform iterative DFS to mark all connected land cells

    return islands


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    print(count_islands(grid))
