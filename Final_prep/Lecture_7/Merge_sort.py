# Описание:
# Merge Sort — это алгоритм сортировки, основанный на принципе разделяй и властвуй. Он разделяет массив на две части, рекурсивно сортирует эти части, а затем объединяет отсортированные подмассивы в один отсортированный массив. Это один из самых стабильных и предсказуемых алгоритмов сортировки с гарантированной сложностью O(nlogn), что делает его очень эффективным для работы с большими массивами данных.
# Принцип работы:
# 1.	Разделение: Исходный массив делится на два подмассива. Процесс разделения продолжается до тех пор, пока не будут получены подмассивы длиной 1, которые уже отсортированы.
# 2.	Слияние: После того как массивы разделены, начинается процесс слияния. Из двух отсортированных подмассивов формируется новый массив, элементы которого упорядочены.
# Алгоритм гарантирует, что время работы будет O(nlogn) в любом случае, что делает его более предсказуемым, чем, например, быстрая сортировка.
# Сложность:
# •	Время:
# o	Лучший, средний и худший случай имеют одинаковую сложность — O(nlogn). Это обусловлено тем, что алгоритм всегда делит массив пополам и выполняет слияние для всех элементов массива.
# •	Пространственная сложность: O(n), так как для слияния требуется дополнительная память для хранения временных массивов.
# Шаги алгоритма:
# 1.	Разделить массив на две части.
# 2.	Рекурсивно применить сортировку слиянием к каждой части.
# 3.	Объединить отсортированные части в один отсортированный массив.
# Преимущества Merge Sort:
# 1.	Гарантированная сложность O(nlogn): В отличие от быстрой сортировки, у которой может быть худший случай O(n^2), сложность сортировки слиянием всегда составляет O(nlogn), что делает её более предсказуемой.
# 2.	Стабильность: Сортировка слиянием является стабильной, то есть элементы с одинаковыми значениями остаются в том же порядке, что и в исходном массиве.
# 3.	Идеален для больших массивов: Благодаря своей стабильной сложности и эффективной работе с большими данными сортировка слиянием используется во многих реальных приложениях, таких как обработка больших файлов или баз данных.
# Недостатки Merge Sort:
# 1.	Пространственная сложность O(n): Алгоритм требует дополнительной памяти для хранения временных массивов во время слияния, что может быть проблемой при работе с очень большими массивами.
# 2.	Меньше эффективен для малых массивов: Для небольших массивов другие алгоритмы, такие как быстрая сортировка или сортировка вставками, могут работать быстрее, так как они требуют меньше памяти и имеют меньший накладной расход.
# Оптимизация Merge Sort:
# 1.	Итеративная версия: Вместо рекурсивной версии можно использовать итеративный подход, чтобы избежать проблем с переполнением стека для очень больших массивов. Однако такая версия сложнее и требует больше кода.
# 2.	Реализация слияния в месте: Если не создавать дополнительные массивы для хранения подмассивов, можно минимизировать использование памяти, но слияние будет более сложным для реализации.
# Заключение: Merge Sort — это стабильный и эффективный алгоритм сортировки, который работает за время O(nlogn) в любых условиях. Он особенно полезен при работе с большими объемами данных, когда важна предсказуемость и стабильность времени выполнения. Однако его пространственная сложность делает его менее подходящим для использования в ограниченных условиях памяти.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the midpoint
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", data)
    merge_sort(data)
    print("Sorted array:  ", data)

