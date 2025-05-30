# Описание: Представление графа является основой для большинства алгоритмов работы с графами, таких как поиск в ширину (BFS), поиск в глубину (DFS), алгоритм Дейкстры и других. В зависимости от задач и особенностей данных, граф можно представлять различными структурами данных, включая список смежности и матрицу смежности. Эти структуры позволяют эффективно хранить и работать с графами для выполнения различных операций.
# 1. Список смежности:
# Список смежности — это структура данных, которая представляет граф в виде массива списков, где для каждой вершины хранится список её соседей. Список смежности является одним из наиболее эффективных способов представления графа, особенно для разреженных графов, в которых количество рёбер значительно меньше максимального возможного.
# Преимущества списка смежности:
# •	Эффективное хранение: Для графов с малым количеством рёбер список смежности занимает меньше памяти, чем матрица смежности.
# •	Динамичность: Добавление и удаление рёбер в списке смежности проще, чем в матрице смежности, потому что мы можем просто добавить или удалить элемент из списка соседей.
# Структура списка смежности:
# Список смежности может быть реализован как массив или список (или словарь в некоторых языках программирования, например, Python), где индекс (или ключ) массива — это вершина, а элементы массива — это список соседей этой вершины.
# Пример:
# Предположим, у нас есть следующий граф с 5 вершинами (0, 1, 2, 3, 4):
#    0 → 1
#    ↘    ↗
#    2 → 3 → 4

# Для этого графа список смежности будет следующим:
# 0: [1, 2]
# 1: [0, 3]
# 2: [0, 3]
# 3: [1, 2, 4]
# 4: [3]
# Здесь:
# •	Вершина 0 соединена с вершинами 1 и 2.
# •	Вершина 1 соединена с вершинами 0 и 3, и так далее.
# Как работает:
# Когда мы хотим узнать, какие вершины смежны с какой-то вершиной, мы просто обращаемся к списку смежности по индексу этой вершины и получаем все её соседние вершины.
# Время выполнения операций:
# •	Поиск всех соседей вершины v: O(k), где k — количество рёбер, исходящих из вершины v.
# •	Поиск ребра между двумя вершинами u и v: O(k), где k — количество рёбер в списке смежности вершины u.
# •	Добавление рёбер: O(1), если мы используем динамический список.
# 2. Матрица смежности:
# Матрица смежности — это двумерная матрица, где строки и столбцы соответствуют вершинам графа, а ячейки матрицы содержат информацию о наличии ребра между вершинами. Это представление удобно, когда граф имеет много рёбер или когда необходимо быстро проверять наличие рёбер между вершинами.
# Преимущества матрицы смежности:
# •	Быстрые операции: Проверка наличия рёбер между двумя вершинами выполняется за O(1), что делает матрицу смежности хорошим выбором для плотных графов.
# •	Простота реализации: Матрица легко реализуется и поддерживает фиксированное количество рёбер, что может быть полезно в некоторых приложениях.
# Структура матрицы смежности:
# Матрица смежности для направленного графа — это квадратная матрица, где каждый элемент A[i][j] равен 1, если существует ребро от вершины i к вершине j, и 0, если такого ребра нет.
# Пример:
# Предположим, тот же граф из предыдущего примера:
#    0 → 1
#    ↘    ↗
#    2 → 3 → 4


# Тогда матрица смежности будет выглядеть так:
#     0  1  2  3  4
# 0 [0, 1, 1, 0, 0]
# 1 [1, 0, 0, 1, 0]
# 2 [0, 0, 0, 1, 0]
# 3 [0, 0, 0, 0, 1]
# 4 [0, 0, 0, 0, 0]

# Здесь:
# •	Строка 0 говорит, что от вершины 0 есть рёбра в вершины 1 и 2.
# •	Строка 1 говорит, что от вершины 1 есть рёбра в вершины 0 и 3, и так далее.
# Как работает:
# Для того чтобы узнать, есть ли ребро между вершинами u и v, нужно просто посмотреть на элемент A[u][v]. Если он равен 1, то ребро существует.
# Время выполнения операций:
# •	Поиск всех соседей вершины v: O(n), где n — количество вершин в графе (так как нужно пройти по всей строке или столбцу).
# •	Поиск рёбер между двумя вершинами u и v: O(1), так как это просто доступ к элементу матрицы.
# •	Добавление рёбер: O(1).
# Когда использовать список смежности:
# •	Для разреженных графов (где количество рёбер значительно меньше n^2).
# •	Когда важно экономить память и при этом выполнять операции с соседями вершины.
# •	Для динамичных графов, в которых часто добавляются или удаляются рёбра.
# Когда использовать матрицу смежности:
# •	Для плотных графов, где количество рёбер близко к n^2, например, в полном графе.
# •	Когда нужно часто проверять наличие рёбер между парами вершин.
# •	Для задач, где важно быстро вычислять наличие рёбер.
