class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def array_to_linked_list(arr):
    sll = SinglyLinkedList()
    for item in arr:
        sll.append(item)
    return sll

def append(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    current = self.head
    while current.next:
        current = current.next
    current.next = new_node

SinglyLinkedList.append = append

def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

SinglyLinkedList.prepend = prepend

sll = array_to_linked_list([1, 2, 3])
sll.append(4)    # Add at end
sll.prepend(0)   # Add at beginning

def delete_value(self, value):
    if not self.head:
        return

    if self.head.data == value:
        self.head = self.head.next
        return

    current = self.head
    while current.next and current.next.data != value:
        current = current.next

    if current.next:
        current.next = current.next.next

SinglyLinkedList.delete_value = delete_value

def insert_after(self, x, data):
    current = self.head
    while current and current.data != x:
        current = current.next
    if current:
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

def insert_before(self, x, data):
    if not self.head:
        return
    if self.head.data == x:
        self.prepend(data)
        return
    current = self.head
    while current.next and current.next.data != x:
        current = current.next
    if current.next:
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

SinglyLinkedList.insert_after = insert_after
SinglyLinkedList.insert_before = insert_before

def print_list(self):
    current = self.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def print_reverse(self):
    def _print_reverse(node):
        if node:
            _print_reverse(node.next)
            print(node.data, end=" <- ")
    _print_reverse(self.head)
    print("None")

SinglyLinkedList.print_list = print_list
SinglyLinkedList.print_reverse = print_reverse

def remove_duplicates(self):
    current = self.head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

SinglyLinkedList.remove_duplicates = remove_duplicates

sll = array_to_linked_list([1, 1, 2, 3, 3, 4])
sll.remove_duplicates()
sll.print_list()

def remove_unsorted_duplicates(self):
    if not self.head:
        return

    seen = set()
    current = self.head
    seen.add(current.data)

    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

SinglyLinkedList.remove_unsorted_duplicates = remove_unsorted_duplicates

sll = array_to_linked_list([3, 1, 4, 1, 2, 3, 4])
print("Before removing duplicates:")
sll.print_list()

sll.remove_unsorted_duplicates()
print("After removing duplicates:")
sll.print_list()

def reverse(self):
    prev = None
    current = self.head

    while current:
        next_node = current.next  # store next node
        current.next = prev       # reverse the link
        prev = current            # move prev forward
        current = next_node       # move current forward

    self.head = prev  # update head to the last node

SinglyLinkedList.reverse = reverse

sll = array_to_linked_list([1, 2, 3, 4, 5])
print("Original List:")
sll.print_list()

sll.reverse()
print("Reversed List:")
sll.print_list()

def reverse_recursive(self):
    def _reverse_recursive(current, prev):
        if not current:
            return prev
        next_node = current.next
        current.next = prev
        return _reverse_recursive(next_node, current)

    self.head = _reverse_recursive(self.head, None)

SinglyLinkedList.reverse_recursive = reverse_recursive

