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
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index - 1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linkedlist = LinkedList(4)
print('Befor appending')
my_linkedlist.print_list()

my_linkedlist.append(5)
my_linkedlist.append(6)
my_linkedlist.append(7)
my_linkedlist.append(8)
my_linkedlist.append(9)
my_linkedlist.append(10)
print('after appending')
my_linkedlist.print_list()

my_linkedlist.pop()
print('after poping the last node')
my_linkedlist.print_list()

my_linkedlist.prepend(3)
print('after append a node in the beginning')
my_linkedlist.print_list()

my_linkedlist.pop_first()
print('after poping the first node')
my_linkedlist.print_list()

index = 2
value = my_linkedlist.get(index).value
print(f'the value at index {index} is {value}')

index1 = 3
value1 = 10
after_set = my_linkedlist.set_value(index1, value1)
print(f'after setting value {value1} at index {index1}, the linkedlist is ')
my_linkedlist.print_list()

index2 = 3
value2 = 7
after_insert = my_linkedlist.insert(index2, value2)
print(f'after inserting {value2} at {index2}, the list is')
my_linkedlist.print_list()

index3 = 4
my_linkedlist.remove(index3)
print(f'after removing the value at index {index3}')
my_linkedlist.print_list()

print('after reversing the linkedlist')
my_linkedlist.reverse()
my_linkedlist.print_list()