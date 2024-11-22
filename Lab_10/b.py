from collections import deque

def shortest_path(n, graph, start, end):
    
    start -= 1
    end -= 1
    
    
    queue = deque([start])
    visited = [False] * n
    distance = [-1] * n
    
   
    visited[start] = True
    distance[start] = 0
    
    
    while queue:
        current = queue.popleft()
        
        for neighbor in range(n):
            if graph[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
                
                
                if neighbor == end:
                    return distance[neighbor]
    
    
    return -1


if __name__ == "__main__":
    n = int(input())  
    graph = [list(map(int, input().split())) for _ in range(n)]
    start, end = map(int, input().split())
    
    
    result = shortest_path(n, graph, start, end)
    print(result)
