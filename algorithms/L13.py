"""
Dijkstra's algorithm

Dijkstra's algorithm is used to find the shortest path 
from a source vertex to all other vertices in a graph with non-negative edge weights.
It works by iteratively selecting the vertex with the minimum tentative distance, 
exploring its neighbors, and updating their distances if a shorter path is found.

Steps:

1.Initialize distances to all vertices as infinity, except for the source vertex (distance = 0).
2.Use a priority queue (or min-heap) to always extract the vertex with the smallest distance.
3.Update the distances of its neighbors.
4.Repeat until all vertices are processed.

Code Implementation:
O(m+n^2)
O(mlogn)implementation with set
O((m+n)logn) implementation with priority queue

Pseudo code:

function Dijkstra(Graph, source):
    for each vertex v in Graph.Vertices:
        dist[v] ← INFINITY      // Изначально расстояние до всех вершин бесконечность
        prev[v] ← UNDEFINED     // Изначально предшественник каждой вершины неопределён
        add v to Q              // Добавляем вершину в очередь с приоритетом

    dist[source] ← 0             // Расстояние до исходной вершины равно 0

    while Q is not empty:       // Пока очередь не пуста
        u ← vertex in Q with min dist[u]  // Извлекаем вершину с минимальным расстоянием
        remove u from Q          // Удаляем её из очереди

        for each neighbor v of u still in Q:   // Для каждого соседа вершины u
            alt ← dist[u] + weight(u, v)      // Рассчитываем альтернативное расстояние через u
            if alt < dist[v]:                 // Если найдено более короткое расстояние
                dist[v] ← alt                // Обновляем расстояние
                prev[v] ← u                 // Обновляем предшественника

    return dist[], prev[]        // Возвращаем массивы расстояний и предшественников

"""

"""
Floyd Algorithm

The Floyd Warshall Algorithm is an all pair shortest path algorithm unlike Dijkstra and Bellman Ford 
which are single source shortest path algorithms. 
This algorithm works for both the directed and undirected weighted graphs. 
But, it does not work for the graphs with negative cycles 
(where the sum of the edges in a cycle is negative).

1.Initialize the solution matrix same as the input 
graph matrix as a first step. 
2.Then update the solution matrix by considering 
all vertices as an intermediate vertex. 
3.The idea is to pick all vertices one by one and updates all 
shortest paths which include the picked vertex as an intermediate vertex in the shortest path. 
4.When we pick vertex number k as an intermediate vertex, 
we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices. 
5.For every pair (i, j) of the source and destination vertices respectively,
 there are two possible cases. 
k is not an intermediate vertex in shortest path from i to j. 
We keep the value of dist[i][j] as it is. 
k is an intermediate vertex in shortest path from i to j. 
We update the value of dist[i][j] as dist[i][k] + dist[k][j], if dist[i][j] > dist[i][k] + dist[k][j]

Pseudo-Code of Floyd Warshall Algorithm :

For k = 0 to n - 1 
    For i = 0 to n - 1 
        For j = 0 to n - 1 
            Distance[i, j] = min(Distance[i, j], Distance[i, k] + Distance[k, j])


where i = source Node, j = Destination Node, k = Intermediate Node

Complexity:
Time Complexity: O(n^3), 
where V is the number of vertices in the graph and we run three nested loops each of size V
Auxiliary Space: O(n^2), 
to create a 2-D matrix in order to store the shortest distance for each pair of nodes.
"""


"""
Ford Bellman Algorithm:

The Bellman-Ford algorithm is used to find the shortest paths from a source vertex to all 
other vertices in a weighted graph. Unlike Dijkstra's algorithm, the Bellman-Ford algorithm
can handle graphs with negative edge weights. Additionally, it can detect negative weight 
cycles (cycles where the sum of edge weights is negative), which makes it more versatile in
certain situations.

Key Features:
Handles negative edge weights: Unlike Dijkstra's, Bellman-Ford 
can work with graphs that have negative edge weights.
Detects negative weight cycles: If there are negative 
weight cycles in the graph, Bellman-Ford can detect them and report them.
Works for directed and undirected graphs.
Not suitable for graphs with negative weight cycles 
because it can keep decreasing the total path cost infinitely.

function BellmanFord(Graph, source):
    // Step 1: Initialize distances
    dist[source] ← 0
    for each vertex v in Graph.Vertices:
        if v ≠ source:
            dist[v] ← ∞      // Set all distances to infinity except the source

    // Step 2: Relax edges (V-1) times
    for i from 1 to V-1:
        for each edge (u, v) in Graph.Edges:
            if dist[u] + weight(u, v) < dist[v]:
                dist[v] ← dist[u] + weight(u, v)

    // Step 3: Check for negative weight cycles
    for each edge (u, v) in Graph.Edges:
        if dist[u] + weight(u, v) < dist[v]:
            return "Graph contains a negative-weight cycle"

    // Step 4: Return the shortest distances
    return dist[]  // Returns the array of shortest distances

Time Complexity:

Best Case: O(m), 
when distance array after 1st and 2nd relaxation are same , we can simply stop further processing.
Average Case: O(n*m)
Worst Case: O(n*m)
"""
