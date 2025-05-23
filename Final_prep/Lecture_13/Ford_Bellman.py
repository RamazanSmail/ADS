# Описание: Алгоритм Форда — Беллмана — это алгоритм для нахождения кратчайших путей в графах, который может работать с графами, содержащими отрицательные веса рёбер. В отличие от алгоритма Дейкстры, который работает только с графами с положительными весами рёбер, алгоритм Форда — Беллмана подходит для работы с отрицательными рёбрами, но не может корректно обработать графы с отрицательными циклами (циклы, где сумма рёбер отрицательна).
# Алгоритм работает путем итеративного релаксации рёбер графа. Он последовательно улучшает оценки кратчайших путей, проверяя все рёбра и обновляя расстояния до вершин.
# ________________________________________
# Шаги алгоритма Форда — Беллмана:
# 1.	Инициализируем расстояния до всех вершин как бесконечность, за исключением начальной вершины, для которой расстояние равно нулю.
# 2.	Для каждой вершины выполняем релаксацию всех рёбер графа (для каждой пары вершин (u,v) с весом ребра w(u,v) проверяем, можно ли уменьшить расстояние до вершины v через вершину u):
# dist[v]=min(dist[v],dist[u]+w(u,v))
# 3.	 Повторяем шаг 2 для всех рёбер V−1 раз (где V — количество вершин). Это гарантирует, что кратчайшие пути будут найдены для графа без отрицательных циклов.
# 4.	  После V−1 итераций, если можно ещё улучшить расстояния, это означает наличие отрицательных циклов
# Объяснение работы алгоритма:
# 1.	Инициализация: Мы начинаем с того, что устанавливаем расстояния от начальной вершины до всех остальных как бесконечности, а для начальной вершины — как 0.
# 2.	Релаксация рёбер: Для каждой вершины мы проверяем все рёбра, и если нахождение пути через вершину u в вершину v даёт более короткий путь, чем уже известный, то обновляем расстояние до вершины v.
# 3.	Проверка на отрицательные циклы: После V−1 итераций (где V — количество вершин), если в графе ещё можно улучшить расстояния, это означает, что существует отрицательный цикл, и алгоритм сообщает об этом.
# Сложность алгоритма:
# •	Время: O(V⋅E), где V — количество вершин, а E — количество рёбер в графе. Мы проводим V−1 итераций, в каждой из которых проверяем все рёбра.
# •	Память: O(V), так как для хранения кратчайших расстояний требуется память для всех вершин графа.
# Применение алгоритма Форда — Беллмана:
# 1.	Графы с отрицательными рёбрами: Этот алгоритм полезен для нахождения кратчайших путей в графах, содержащих рёбра с отрицательными весами, в отличие от алгоритма Дейкстры.
# 2.	Поиск путей в графах с отрицательными циклами: Алгоритм может быть использован для обнаружения отрицательных циклов в графах, что может быть важным для анализа транспортных и финансовых сетей.
# 3.	Финансовые расчёты: В задачах, связанных с анализом финансовых потоков, где могут быть отрицательные значения, этот алгоритм может быть применим для расчёта оптимальных путей.
# 4.	Теория графов: Этот алгоритм активно используется в теории графов и математическом моделировании для работы с графами с отрицательными рёбрами и анализа их структуры.
def bellman_ford(vertices, edges, start):
    # Initialize distances from start to all vertices as infinity
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    # Relax edges repeatedly
    for _ in range(len(vertices) - 1):
        updated = False
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                updated = True
        if not updated:
            break

    # Check for negative-weight cycles
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            raise Exception("Graph contains a negative weight cycle")

    return distances
