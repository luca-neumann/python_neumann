import random

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_last(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def get_length(self):
        return self.length

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print("None")

    def __iter__(self):
        self._iter_node = self.head
        return self

    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        value = self._iter_node.value
        self._iter_node = self._iter_node.next
        return value

if __name__ == "__main__":
    linked_list = LinkedList()
    for _ in range(5):
        linked_list.add_last(random.randint(1, 100))
    
    print("Linked List:")
    linked_list.print_list()
    print("Länge der Liste:", linked_list.get_length())
    
    print("Iterieren durch die Liste:")
    for value in linked_list:
        print(value)
