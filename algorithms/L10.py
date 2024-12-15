"""
Adjacency List
What it is: A list where each node has a list of its adjacent (connected) nodes.

How it works:

Each vertex is a key in a dictionary.
The value is a list of vertices that are directly connected to the key vertex.

Pros:

Memory-efficient for sparse graphs (fewer edges).
Easy to iterate over neighbors of a vertex.
Cons:

Checking for the existence of a specific edge is slower (
O(k), where 
k is the number of neighbors).

Adjacency Matrix
What it is: A 2D matrix where rows and columns represent vertices, and the cell value indicates if an edge exists.

How it works:

For a graph with 
n vertices, create an 
n×n matrix.
If an edge exists between vertex 
i and 
j, set matrix[i][j] = 1 (or the edge weight for weighted graphs).
Otherwise, matrix[i][j] = 0.

Pros:

Fast edge look-up (
O(1)).
Suitable for dense graphs.
Cons:

Memory-inefficient for sparse graphs.
Iterating over all neighbors of a vertex is slower (
O(n)).

Edge List
What it is: A list of all edges in the graph.
How it works:
Each edge is represented as a pair (or triplet for weighted graphs).

Pros:
Simple to implement.
Space-efficient for listing all edges.
Cons:
Slow for certain operations, like finding neighbors or checking for specific edges.

 Breadth-First Search (BFS)
BFS is a graph traversal algorithm that explores all neighbors of a vertex before moving to the next level of neighbors.

How BFS Works
Start at the source node and mark it as visited.
Use a queue to keep track of nodes to visit next.
While the queue is not empty:
Dequeue a node.
Visit all its unvisited neighbors and add them to the queue.
Repeat until all reachable nodes are visited.


d[i, n] = infinity
d[s] = 0
pr[s] == -1        //Индекс отца начальной врешины pr равен -1 так как s самая первая вершина, 
Q.push(s)          // соотвественно мы добавляем в очередь начальный индекс
while(!Q.empty):   //пока очередь не пустая
    V = Q.front() Q.pop()     //V is vertex(вершина), рассматриваем передний элемент и удаляем что бы уже не смотреть
    for i in G[V]:     // проходимся по графу G и пока дистанция между соседями неизвестна 
        if(d[i] == infinity):  
            d[i] = d[v] + 1     //записываем эту дистанцию как наша дистанция на данный момент + 1
            Q.push(i)           //добавляем в очередь   
            pr[i] = V           // записываем что отец этой вершины равен начальной вершины от которой вышли другие



  2     6
 /  \  /  \
1    4     7
 \  /     /
  3 ---- 5

в данном примере начальная вершина это 1, далее смотрим что следующая дистанция не записана, поэтому мы пишем
что дистанция до 2 равна d[v] + 1. Далее видим что есть еще одна вершина с неизвестным расстоянием это 3.
Мы проверяем её также как и 2 и записываем дистанцию до этой вершины, она также равна d[v] + 1.
С 4 немного по-другому, мы смотрим что от 2 есть неизвестная еще вершина это 4, записываем и когда смотрим 
что больше неизвестных вершин от 2 нет, смотри 3ку. Там выходит что дистанция до 4 уже есть поэтому условие
if мы пропускаем. и так далее мы проверяем всем вершины.
Time complexity: O(V + E)
"""

"""
Graph Representations:
Adjacency List:
Efficient for sparse graphs.
Easy to retrieve neighbors of a vertex.
Well-suited for traversal algorithms like BFS and DFS.
Adjacency Matrix:
Provides fast edge existence checks.
Suitable for dense graphs with many edges.
Requires more memory and is less efficient for sparse graphs.
Edge List:
Simple representation of edges.
Ideal for edge-focused algorithms like Kruskal's MST.
Less convenient for graph traversal tasks.
2. BFS (Breadth-First Search):
BFS is an algorithm used to:

Find all vertices reachable from a start vertex.
Determine the shortest path in unweighted graphs.
Check graph connectivity.
Advantages of BFS:

Easy to implement with a queue.
Efficient for level-order exploration of graphs.
Complexity:

For adjacency list: 
O(V+E), where 

V is the number of vertices and 

E is the number of edges.
For adjacency matrix: 

O(V^2), less efficient for sparse graphs.
Summary
Choosing the right graph representation depends on the graph's density and the problem being solved:

Adjacency List is a versatile and efficient representation for most tasks, especially for sparse graphs.
Adjacency Matrix is better suited for dense graphs or scenarios where edge existence checks are frequent.
Edge List is ideal for edge-centric algorithms like minimum spanning tree construction.
BFS is a fundamental graph traversal algorithm valued for its efficiency and simplicity, making it an essential tool for graph-related problems.
"""

def create_adjacency_list(edges):
    graph = {}  # Инициализируем пустой граф (словарь)
    for u, v in edges:
        if u not in graph:
            graph[u] = []  # Добавляем вершину, если её нет в графе
        if v not in graph:
            graph[v] = []  # То же самое для другой вершины
        graph[u].append(v)  # Добавляем ребро u -> v
        graph[v].append(u)  # Добавляем ребро v -> u для неориентированного графа
    return graph

def create_adjacency_matrix(vertices, edges):
    n = len(vertices)
    matrix = [[0 for _ in range(n)] for _ in range(n)]  # Создаём матрицу n x n, заполненную 0
    vertex_to_index = {vertex: i for i, vertex in enumerate(vertices)}  # Сопоставляем вершины с индексами

    for u, v in edges:
        i, j = vertex_to_index[u], vertex_to_index[v]
        matrix[i][j] = 1  # Добавляем ребро u -> v
        matrix[j][i] = 1  # Для неориентированного графа добавляем v -> u

    return matrix

def create_edge_list(edges):
    return edges  # Возвращаем список рёбер
