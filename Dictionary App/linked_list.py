class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, initial_data=None):
        self.head = None
        if initial_data:
            for data in initial_data:
                self.append(data)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def append_and_sort(self, data):
        self.append(data)
        self.sort()

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def sort(self):
        if not self.head:
            return

        elements = self.to_list()
        elements.sort(key=lambda x: x['english'].lower())

        self.head = Node(elements[0])
        current = self.head
        for element in elements[1:]:
            current.next = Node(element)
            current = current.next

    def insert_sorted(self, data):
        new_node = Node(data)
        if not self.head or data['english'].lower() <= self.head.data['english'].lower():
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and data['english'].lower() > current.next.data['english'].lower():
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False