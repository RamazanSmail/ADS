from collections import deque

def mario_war(grid):
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    m = len(grid)  
    n = len(grid[0])  
    
    queue = deque()
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
    
    minutes = 0  
    
    
    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            
           
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2  
                    queue.append((nx, ny))
        
        
        if queue:
            minutes += 1
    
    
    for row in grid:
        if 1 in row:
            return -1  
    
    return minutes


if __name__ == "__main__":
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    
    
    result = mario_war(grid)
    print(result)

