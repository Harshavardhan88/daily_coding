# singly linked list - basic operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def show(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        print(" -> ".join(items))


numbers = LinkedList()
numbers.add_end(10)
numbers.add_end(20)
numbers.add_end(30)
numbers.show()

numbers.add_start(5)
numbers.show()

print(numbers.search(20))
print(numbers.search(99))

numbers.delete(20)
numbers.show()
