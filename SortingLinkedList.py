class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def bubble_sort(self):
        if self.length < 2:
            return
        end = None
        while end != self.head.next:
            current = self.head
            while current.next != end:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                current = current.next
            end = current

    def selection_sort(self):
        if self.length < 2:
            return
        current = self.head
        while current is not None:
            smallest = current
            next_node = current.next
            while next_node is not None:
                if next_node.value < smallest.value:
                    smallest = next_node
                next_node = next_node.next
            if current != smallest:
                current.value, smallest.value = smallest.value, current.value
            current = current.next
    
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.print_list()

print('\nafter sorting')
#my_linked_list.bubble_sort()
my_linked_list.selection_sort()
my_linked_list.print_list()
