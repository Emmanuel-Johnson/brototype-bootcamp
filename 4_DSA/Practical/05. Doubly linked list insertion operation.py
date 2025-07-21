class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def add_at_begin(self, data):
        newnode = Node(data)
        newnode.next = self.head
        if self.head:
            self.head.prev = newnode
        self.head = newnode
        
    def add_at_end(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
        newnode.prev = current
        
    def array_to_dll(self, arr):
        for i in arr:
            self.add_at_end(i)
        print("Converted Successfully")
        
    def print_forward(self):
        if self.head is None:
            print("Doubly Linked list is empty")
            return
        current = self.head
        while current:
            print(current.data, end = " --> ")
            current = current.next
        print("None")
        
    def print_reverse(self):
        if self.head is None:
            print("Doubly Linked list is empty")
            return
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end = " <-- ")
            current = current.prev
        print("None")
    
    def delete_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
    
    def insert_after(self, x, data):
        current = self.head
        while current:
            if current.data == x:
                newnode = Node(data)
                newnode.next = current.next
                newnode.prev = current
                if current.next:
                    current.next.prev = newnode
                current.next = newnode
                return
            current = current.next
        print(f"{x} not found.")
    
    def insert_before(self, x, data):
        current = self.head
        while current:
            if current.data == x:
                newnode = Node(data)
                newnode.next = current
                newnode.prev = current.prev
                if current.prev:
                    current.prev.next = newnode
                else:
                    self.head = newnode
                current.prev = newnode
                return
            current = current.next
    
    def remove_duplicates(self):
        seen = set()
        current = self.head
        while current:
            if current.data in seen:
                next_node = current.next
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                current = next_node
            else:
                seen.add(current.data)
                current = current.next
       
       
dll = DoublyLinkedList()

arr = [1, 2, 2, 1, 3, 4, 5, 6, 4, 5]
dll.array_to_dll(arr)
dll.remove_duplicates()
dll.print_forward()
