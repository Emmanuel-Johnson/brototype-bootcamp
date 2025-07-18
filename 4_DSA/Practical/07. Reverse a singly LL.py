class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
    
    def add_at_beginning(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        
    def add_at_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
    
    def array_to_sll(self, arr):
        for i in arr:
            self.add_at_end(i)
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' --> ')
            current = current.next
        print("None")
    
    def delete(self, data):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print(f"{data} not found in the linked list")
    
    def insert_node_before_data(self, before, data):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == before:
            self.add_at_beginning(data)
            return
        current = self.head
        while current.next:
            if current.next.data == before:
                newnode = Node(data)
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next
        print(f"{before} not found in the linked list")
        
    def insert_node_after_data(self, after, data):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            if current.data == after:
                newnode = Node(data)
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next
        print(f"{data} not found in the linked list")
    
    def print_reverse(self):
        def _print_reverse(node):
            if not node:
                return
            _print_reverse(node.next)
            print(node.data, end = ' <-- ')
        _print_reverse(self.head)
        print("None")
        
    def print_reverse_iteration(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        while stack:
            print(f"{stack.pop()}", end = " <-- ")
        print("None")
        
        
        
sll = SLL()

arr = [1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 3, 3, 3, 2, 1]
sll.array_to_sll(arr)
sll.display()
