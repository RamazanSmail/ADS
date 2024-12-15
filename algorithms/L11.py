"""
DFS (Depth-First Search) is a graph traversal algorithm that explores as far along each branch of a 
graph as possible before backtracking to explore alternative paths.
How DFS Works
Start the traversal:
Begin at the starting vertex.
Mark it as visited.
Explore deeper:
Select one of the current vertex's unvisited neighbors and move to it.
Backtrack:
If the current vertex has no unvisited neighbors, backtrack to the previous vertex.
Repeat:
Continue the process until all vertices have been explored.

 Complexity
Time Complexity: O(V+E), where 
V is the number of vertices and E is the number of edges.
Each vertex and edge is visited once.
Space Complexity:
Recursive version: O(V) due to the call stack.
Iterative version: O(V) for the stack storage.

Advantages of DFS
Efficiency: Flexibility: Foundation for Other Algorithms:

Disadvantages of DFS
Stack Depth:
No Shortest Path Guarantee:
Complex Iterative Implementation:

Реализация DFS
Итеративный способ (с использованием стека):

//DFS - поиск в глубину
bool was[v] //начальная вершина
dfs(v):    
    was[v] = 1  //отмечает вершину как посещенную
    for(v, u):  //u сосед посещенной вершины
        if(!was[u]):   //если этот сосед не посещен, мы запускаем дфс от этого соседа
            dfs(u)   




  2     6            //Как бы проходил BFS: 1 2 3 4 5 6 7
 /  \  /  \          //Как бы проходил DFS: 1 2 4 6 7 3 5
1    4     7
 \  /     /
  3 ---- 5

Главное отличие DFS от BFS в том что DFS грубо говоря заходит до конца, и идет обратно пока не найдет вершину
где есть не посещенный сосед, и дальше запустит DFS рекурсивно.
Time complexity: O(V + E)
"""

"""
Рекурсивный способ:
python
Копировать код

"""

"""
Topological Sort is a linear ordering of the vertices in a
 Directed Acyclic Graph (DAG) such that for every directed edge 
u→v, vertex u comes before vertex v in the ordering.

Topological sort is used in problems involving dependencies where 
certain tasks must be performed before others. Common applications include:

Task scheduling (e.g., prerequisites in courses).
Compilation order of files.
Dependency resolution in software libraries.

Time Complexity
DFS-Based:
Time: O(V+E), where V is vertices and E is edges.
Space: O(V) for stack and visited set.

Advantages
Efficient: Both DFS and Kahn’s algorithms run in O(V+E).
Handles Dependencies: Excellent for scheduling tasks with prerequisites.
Simple to Implement: Especially the DFS-based approach.

Disadvantages
Limited to DAGs: Cannot be applied to graphs with cycles.
Cycle Detection: Requires additional checks or handling (e.g., in Kahn’s algorithm).

Topological_sort
dfs(v, ts):   //vertex and topsort vector
    was[v] = 1  //отмечаем начальную вершину посещенной
    for(v, u):  //ищем соседей начальной вершины
        if(!was[u]):    //если сосед не посещен
            dfs(u, ts)  //запускаем топ сорт уже от соседа
    ts.push_back(v)     //добавляем в конец вектора вершину

int main():
    for i in range(1, n):
        if(!was[i]):
            dfs(i, ts):
    reverse(ts)       



all this vertexes points down
6   4   8            
 \ / \ / \
  1   3   |       ts: 5, 7, 1, 2, 3, 6, 8  then we reverse
 / \ / \  /
5   7   2
Time complexity: O(V + E)
"""