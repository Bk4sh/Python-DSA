class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinearySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def BreadthFirstSearch(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result
    
    def DFS_PreOrder(self):
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
    def DFS_PostOrder(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result
    
    def DFS_InOrder(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
    def is_valid_BST(self):
        node_values = self.DFS_InOrder()
        for i in range(1, len(node_values)):
            if node_values[i] <= node_values[i-1]:
                return False
        return True


my_tree = BinearySearchTree()
print(my_tree.root)

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print('\nafter inserting')
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.root.left.left.value)
print(my_tree.root.left.right.value)
print(my_tree.root.right.left.value)
print(my_tree.root.right.right.value)

print('\nchecking if a value is present or not')
print(my_tree.contains(27))
print(my_tree.contains(17))

print('\nBreadth First Search')
print(my_tree.BreadthFirstSearch())

print('\nDepth First Search PreOrder')
print(my_tree.DFS_PreOrder())

print('\nDepth First Search PostOrder')
print(my_tree.DFS_PostOrder())

print('\nDepth First Search InOrder')
print(my_tree.DFS_InOrder())

print('\nchecking if it is a valid BST or not')
print(my_tree.is_valid_BST())