"""
Prim's Algorithm:

Purpose: To find the Minimum Spanning Tree (MST) of a connected, weighted graph.

Approach: A greedy algorithm that starts from an arbitrary vertex and iteratively 
adds the minimum weight edge connecting the selected vertices to the rest, 
until all vertices are included in the MST.

Steps:
Start from an arbitrary vertex and add it to the MST.
Add all edges incident to the selected vertex to a priority queue (sorted by weight).
Extract the minimum weight edge from the queue. If it connects a new vertex to the MST, add that vertex to the tree.
Repeat the process until all vertices are included in the MST.

Time Complexity:
Worst case (dense graph): O(n^2+m),O(m log n), where E is the number of edges and V is the number of vertices.
Best case (sparse graph, like a tree):priority queue O(m log n), since the number of edges is much smaller.
Implementation with adjancecy matrix T.C: O(n^3)
for adjancency list implementation:O(m+n)*O(Logn) which is O((m+n)*Logn) = O(mLogn) 

Data Structures:
A priority queue (min-heap) is used to efficiently find and update the minimum weight edge.

Key Features:
Greedy approach: Always chooses the minimum weight edge at each step.
Guarantees that the resulting tree is the MST with the smallest total weight.

Pseudo code of Prim's algorithm
for all u in V:
cost(u) =∞
prev(u) = nil
Pick any initial node uo
cost(u0) = 0
H = makequeue (V)
(priority queue, using cost-values as keys)
while H is not empty:
v = deletemin(H)
for each {v, z} € E:
if cost(z) > w(v, z):
cost(z) = w(v, z)
prev(z) = v
decreasekey(H, z)
"""




       
"""
Kruskal's Algorithm:

Goal: To construct the minimum spanning tree (MST) for a connected weighted graph.
Working Principle: A greedy algorithm that adds the edges with the smallest weights to the MST,
 as long as adding an edge does not form a cycle, until the tree spans all vertices.

Steps:
Sort all edges in non-decreasing order of their weights.
Initialize a Union-Find structure to track connected components.

Iterate through the edges:
If the edge connects two different components (no cycle), add it to the MST.
If the edge connects two vertices within the same component (cycle formed), skip it.
Repeat until the MST contains V-1 edges, where V is the number of vertices.

Time Complexity:
Worst and Best Case: O(E log E), where E is the number of edges (due to sorting the edges).
Union and Find operations with optimizations are O(α(V)), where α is the very 
slow-growing inverse Ackermann function, 
almost constant in practice.

Data Structures:
Union-Find (or Disjoint Set) — a structure for efficiently managing connected components with 
Find and Union operations.

Key Features:
Greedy: At each step, the algorithm chooses the edge with the smallest weight that does not form a cycle.
Guaranteed Minimum Tree: The algorithm always produces the minimum spanning tree for a connected weighted graph.
The algorithm is independent of the starting vertex.

Kruscal(G):
A = empty.set
For each vertex v in G.V:
 Make-set(v)
For each edge (u,v) ordered by increasing order by weight(u,v):
if Find-Set(u)!= Find-Set(v):
A = A {(u,v)}
UNION(u,v)
return A
"""
