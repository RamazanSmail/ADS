# Связанный список — это структура данных, состоящая из узлов (элементов), каждый из которых содержит 
# данные и указатель (ссылку) на следующий узел в последовательности. Связанные списки используются 
# для хранения динамических наборов данных и обладают гибкостью в управлении памятью.

# Преимущества связанных списков
# •	Эффективное управление памятью: список может расти и уменьшаться по мере необходимости.
# •	Быстрая вставка и удаление узлов.
# •	Нет необходимости заранее выделять память.
# Недостатки связанных списков
# •	Доступ к элементу занимает O(n), так как необходимо пройти список.
# •	Затраты на хранение указателей увеличивают объем используемой памяти.
# •	Более сложная реализация по сравнению с массивами.

# Node class for a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node

    # Method to insert a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node

    # Method to delete a node by value
    def delete_node(self, key):
        current = self.head

        # If the node to be deleted is the head node
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Find the node to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print("Key not found in the list")
            return

        # Unlink the node
        prev.next = current.next
        current = None

    # Method to search for a node in the list
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Method to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example Usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_end(30)
    sll.insert_at_beginning(5)

    print("Linked List:")
    sll.display()

    print("\nDeleting 20:")
    sll.delete_node(20)
    sll.display()

    print("\nSearching for 10:", sll.search(10))
    print("Searching for 50:", sll.search(50))
