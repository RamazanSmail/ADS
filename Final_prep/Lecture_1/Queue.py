#Преимущества очереди
# •	Простота реализации.
# •	Эффективность операций (если не требуется сдвигать элементы, как в списках).
# Недостатки очереди
# •	Ограниченный доступ: можно работать только с началом и концом очереди.
# •	Если очередь реализована на массиве, она может быть ограничена по размеру.
# Работает по принципу FIFO(First in First Out)
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Добавить элемент в очередь"""
        self.items.append(item)

    def dequeue(self):
        """Удалить элемент из очереди и вернуть его"""
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("dequeue from empty queue")

    def front(self):
        """Посмотреть первый элемент очереди"""
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        """Проверить, пуста ли очередь"""
        return len(self.items) == 0

    def size(self):
        """Получить размер очереди"""
        return len(self.items)


# Пример использования
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Первый элемент:", queue.front())  # 10
print("Размер очереди:", queue.size())  # 3
print("Удаленный элемент:", queue.dequeue())  # 10
print("Очередь пуста?", queue.is_empty())  # False
