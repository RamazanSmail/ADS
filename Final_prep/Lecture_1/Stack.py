# Преимущества стека
# •	Простота реализации.
# •	Высокая производительность (операции O(1)).
# Недостатки стека
# •	Ограниченный доступ: можно работать только с верхним элементом.
# •	Может быть ограничен по размеру (если реализован на основе массива).
# Работает по принципу LIFO(Last in first out)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавить элемент в стек"""
        self.items.append(item)

    def pop(self):
        """Удалить элемент из стека и вернуть его"""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        """Посмотреть верхний элемент стека"""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        """Проверить, пуст ли стек"""
        return len(self.items) == 0

    def size(self):
        """Получить размер стека"""
        return len(self.items)


# Пример использования
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Верхний элемент:", stack.peek())  # 30
print("Размер стека:", stack.size())    # 3
print("Удаленный элемент:", stack.pop())  # 30
print("Стек пустой?", stack.is_empty())   # False

