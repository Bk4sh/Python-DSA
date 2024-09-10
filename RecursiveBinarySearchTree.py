class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinearySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left =  self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    def delete_node(self, value):
        self.__delete_node(self.root, value)

my_tree = BinearySearchTree()
print(my_tree.root)

my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)
print('\nafter inserting')
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.root.left.left.value)
print(my_tree.root.left.right.value)
print(my_tree.root.right.left.value)
print(my_tree.root.right.right.value)

print('\nBST contains 27')
print(my_tree.r_contains(27))

print('\nminimum value in left')
print(my_tree.min_value(my_tree.root))
print(my_tree.min_value(my_tree.root.right))

print('\nafter deleteing 21')
my_tree.delete_node(47)
print('\nroot: ', my_tree.root.value)
print('\nroot->left: ', my_tree.root.left.value)
print('\nroot->right: ', my_tree.root.right.value)
print('\nroot->left->left: ', my_tree.root.left.left)
print('\nroot->left->right: ', my_tree.root.left.right.value)
print('\nroot->right->left: ', my_tree.root.right.left.value)
print('\nroot->right->right: ', my_tree.root.right.right.value)