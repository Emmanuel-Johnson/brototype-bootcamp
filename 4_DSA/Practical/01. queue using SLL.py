# queue using SLL 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class QueueUsingSLL:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        newnode = Node(data)
        if self.front is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode
        print("Enqueued Successfully")
        
    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed
    
    def is_empty(self):
        return self.front is None
        
    def peek(self):
        if self.front is None:
            return "Queue is Empty"
        return self.front.data
        
    def display(self):
        current = self.front
        while current:
            print(current.data, end = " --> ")
            current = current.next
        print("None")
    
q = QueueUsingSLL()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()         # Output: 10 -> 20 -> 30 -> None

print(q.dequeue())  # Output: 10
q.display()         # Output: 20 -> 30 -> None

print(q.peek())     # Output: 20
