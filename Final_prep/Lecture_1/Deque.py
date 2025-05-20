# Преимущества двусторонней очереди
# 1.	Гибкость: поддерживает операции добавления и удаления с обеих сторон.
# 2.	Быстрота: операции O(1) для вставки и удаления с обоих концов (при реализации на связных списках или в deque из collections).
# Недостатки двусторонней очереди
# 1.	Может занимать больше памяти, чем требуется, особенно если реализована на массиве.
# 2.	Ограниченный доступ: нельзя обращаться к элементам, кроме первого и последнего.
from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def append(self, item):
        """Добавить элемент в конец"""
        self.items.append(item)

    def appendleft(self, item):
        """Добавить элемент в начало"""
        self.items.appendleft(item)

    def pop(self):
        """Удалить элемент с конца и вернуть его"""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty deque")

    def popleft(self):
        """Удалить элемент с начала и вернуть его"""
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("popleft from empty deque")

    def front(self):
        """Посмотреть первый элемент"""
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def back(self):
        """Посмотреть последний элемент"""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        """Проверить, пуста ли очередь"""
        return len(self.items) == 0

    def size(self):
        """Получить размер очереди"""
        return len(self.items)


# Пример использования
deque = Deque()
deque.append(10)
deque.append(20)
deque.appendleft(5)
print("Первый элемент:", deque.front())  # 5
print("Последний элемент:", deque.back())  # 20
print("Размер очереди:", deque.size())  # 3
print("Удален первый элемент:", deque.popleft())  # 5
print("Удален последний элемент:", deque.pop())  # 20

