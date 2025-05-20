# Время выполнения операций для двусвязного списка зависит от конкретной операции:
# 1.	Добавление элемента в конец (append):
# 	Время: O(1), если мы храним указатель на последний элемент списка (что реализовано в нашем примере). 
#     Мы просто добавляем новый узел в конец, обновляя указатель хвоста.
# 	Если список не хранит указатель на хвост, то добавление в конец будет требовать обхода списка, что 
#     даст время O(n).
# 2.	Добавление элемента в начало (prepend):
# 	Время: O(1), так как для добавления нового элемента в начало достаточно обновить указатели головы и 
#     следующего узла.
# 3.	Удаление элемента (delete):
# 	Время: O(n) в худшем случае, если элемент нужно искать. В случае, если узел найден, удаление происходит 
#     за O(1), так как мы просто обновляем указатели предыдущего и следующего узлов.
# 4.	Перебор всех элементов списка (display):
# 	Время: O(n), так как необходимо пройти по всем узлам списка для их вывода.

# Класс узла для двойного связанного списка
class Node:
    def __init__(self, data):
        self.data = data  # Данные узла
        self.next = None  # Ссылка на следующий узел
        self.prev = None  # Ссылка на предыдущий узел


# Класс двойного связанного списка
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Указатель на начало списка

    # Вставка узла в начало списка
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:  # Если список пуст
            self.head = new_node
            return
        new_node.next = self.head  # Ссылка нового узла на текущую голову
        self.head.prev = new_node  # Ссылка текущей головы на новый узел
        self.head = new_node  # Новый узел становится головой

    # Вставка узла в конец списка
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # Если список пуст
            self.head = new_node
            return
        current = self.head
        while current.next:  # Переходим к последнему узлу
            current = current.next
        current.next = new_node  # Связываем последний узел с новым
        new_node.prev = current  # Связываем новый узел с предыдущим

    # Удаление узла по значению
    def delete_node(self, key):
        if not self.head:  # Если список пуст
            print("Список пуст")
            return

        current = self.head

        # Если голова содержит искомое значение
        if current.data == key:
            if current.next:  # Если есть следующий узел
                current.next.prev = None
            self.head = current.next  # Сдвиг головы
            current = None
            return

        # Поиск узла с заданным значением
        while current and current.data != key:
            current = current.next

        # Если узел не найден
        if not current:
            print("Узел с заданным значением не найден")
            return

        # Удаление узла
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        current = None

    # Отображение списка
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Пример использования
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(5)
    dll.insert_at_end(20)
    dll.insert_at_end(30)

    print("Двойной связанный список:")
    dll.display()

    print("\nУдаление узла со значением 20:")
    dll.delete_node(20)
    dll.display()
