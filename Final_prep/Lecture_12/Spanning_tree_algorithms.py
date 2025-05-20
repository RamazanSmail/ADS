# Описание:
# Алгоритмы поиска минимального остовного дерева (MST, от англ. Minimum Spanning Tree) используются для нахождения дерева, которое охватывает все вершины графа с минимальной суммой весов рёбер. Для неориентированных графов существует несколько алгоритмов для поиска минимального остовного дерева. Два наиболее известных алгоритма — это алгоритм Краскала и алгоритм Прима.
# 1. Алгоритм Краскала:
# Алгоритм Краскала строит минимальное остовное дерево путём сортировки рёбер по весу и добавления рёбер в дерево, при этом избегая образования циклов. Он эффективно работает с графами, представленными списками рёбер.
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False  # Already connected

        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True

def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)

    mst = []
    mst_cost = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            mst_cost += weight

    return mst_cost, mst

# Example usage
vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 1),
    ('C', 'D', 4)
]

mst_cost, mst = kruskal(vertices, edges)
print("MST Cost:", mst_cost)
print("MST Edges:", mst)

# 2. Алгоритм Прима:
# Алгоритм Прима начинает с одной вершины и поочерёдно добавляет к остовному дереву рёбра с минимальным весом, расширяя дерево. Алгоритм Прима эффективен при работе с графами, представленными матрицами смежности.
# ________________________________________
# 1. Алгоритм Краскала
# Алгоритм Краскала — это жадный алгоритм, который строит минимальное остовное дерево путём последовательного добавления рёбер с наименьшим весом. Важной частью алгоритма является использование структуры данных "система непересекающихся множеств" (Union-Find), которая позволяет эффективно отслеживать и объединять компоненты связности.
# Шаги алгоритма Краскала:
# 1.	Сортировка рёбер графа по весу.
# 2.	Инициализация пустого дерева.
# 3.	Поочерёдное добавление рёбер в дерево, если они не образуют цикл (с помощью Union-Find).
# 4.	Алгоритм завершён, когда дерево охватывает все вершины.
# Алгоритм Прима
# Алгоритм Прима работает с графом, добавляя рёбра к остовному дереву, начиная с произвольной вершины. Он использует структуру данных минимальная очередь (например, кучу), чтобы на каждом шаге выбирать ребро с минимальным весом, которое соединяет дерево с новой вершиной.
# Шаги алгоритма Прима:
# 1.	Начинаем с произвольной вершины.
# 2.	Добавляем рёбра, которые соединяют вершины в дереве с вершинами вне дерева, и выбираем ребро с минимальным весом.
# 3.	Повторяем шаг 2, пока все вершины не будут включены в дерево.
import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, node)
    mst_cost = 0
    mst_edges = []

    while min_heap and len(visited) < len(graph):
        weight, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        mst_cost += weight

        # Avoid adding the initial dummy edge (0, start)
        if weight != 0:
            mst_edges.append((prev_node, node, weight))

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor))
                # Save the edge’s origin for tracking MST edges
                prev_node = node

    return mst_cost, mst_edges

# Example usage: undirected weighted graph (adjacency list)
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)],
}

mst_cost, mst_edges = prim(graph, 'A')
print("MST Cost:", mst_cost)
print("MST Edges:", mst_edges)
# Сложность алгоритмов:
# •	Алгоритм Краскала:
# o	Время: O(ElogE), где E — количество рёбер, так как необходимо отсортировать рёбра.
# o	Память: O(V+E), где V — количество вершин, для хранения рёбер и структуры Union-Find.
# •	Алгоритм Прима:
# o	Время: O(ElogV), где E — количество рёбер, V — количество вершин, так как для каждого рёбра мы выполняем операцию извлечения минимального элемента из кучи.
# o	Память: O(V+E), где V — количество вершин, для хранения графа и очереди с приоритетами.
# ________________________________________
# Применение алгоритмов:
# 1.	Алгоритм Краскала лучше всего работает с графами, где рёбер много, а количество вершин относительно невелико.
# 2.	Алгоритм Прима предпочтительнее при работе с плотными графами (где количество рёбер близко к квадрату количества вершин).
