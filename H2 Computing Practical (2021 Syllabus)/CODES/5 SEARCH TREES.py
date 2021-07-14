from random import randint

lst = [randint(1, 100) for _ in range(10)]

print("List:", lst)
print()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node

class BinarySearchTree: # binary search tree, OOP
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            curr_node = self.root
            while curr_node:
                if data < curr_node.get_data(): # left
                    if curr_node.get_left() == None:
                        curr_node.set_left(Node(data))
                        curr_node = None
                    else:
                        curr_node = curr_node.get_left()
                else: # right
                    if curr_node.get_right() == None:
                        curr_node.set_right(Node(data))
                        curr_node = None
                    else:
                        curr_node = curr_node.get_right()
        
    def search(self, data):
        curr_node = self.root
        while curr_node:
            if data == curr_node.get_data():
                return True
            elif data < curr_node.get_data(): # left
                curr_node = curr_node.get_left()
            else: # right
                curr_node = curr_node.get_right()
        return False

    def height(self):
        def helper(curr_node):
            if curr_node == None:
                return -1
            else:
                return 1 + max(helper(curr_node.get_left()), helper(curr_node.get_right()))
        return helper(self.root)

    def inorder_traversal(self): # left, display, right
        def helper(curr_node):
            if curr_node == None:
                return []
            else:
                return helper(curr_node.get_left()) + [curr_node.get_data()] + helper(curr_node.get_right())
        def helper2(curr_node):
            if curr_node:
                if curr_node.get_left():
                    helper2(curr_node.get_left())
                    
                print(curr_node.get_data())

                if curr_node.get_right():
                    helper2(curr_node.get_right())
        helper2(self.root)
        return helper(self.root)

    def preorder_traversal(self): # display, left, right
        def helper(curr_node):
            if curr_node == None:
                return []
            else:
                return [curr_node.get_data()] + helper(curr_node.get_left())  + helper(curr_node.get_right())
        def helper2(curr_node):
            if curr_node:
                print(curr_node.get_data())
                
                if curr_node.get_left():
                    helper2(curr_node.get_left())

                if curr_node.get_right():
                    helper2(curr_node.get_right())
        helper2(self.root)
        return helper(self.root)

    def postorder_traversal(self): # left, right, display
        def helper(curr_node):
            if curr_node == None:
                return []
            else:
                return helper(curr_node.get_left())  + helper(curr_node.get_right()) + [curr_node.get_data()]
        def helper2(curr_node):
            if curr_node:
                if curr_node.get_left():
                    helper2(curr_node.get_left())

                if curr_node.get_right():
                    helper2(curr_node.get_right())
                
                print(curr_node.get_data())
        helper2(self.root)
        return helper(self.root)

binary_search_tree = BinarySearchTree()

for item in lst:
    binary_search_tree.insert(item)

print(f"Search for {lst[0]}:", binary_search_tree.search(lst[0]))
print(f"Search for 0:", binary_search_tree.search(0))

print("Height of binary search tree:", binary_search_tree.height())

print("Inorder traversal:", binary_search_tree.inorder_traversal())
print("Preorder traversal:", binary_search_tree.preorder_traversal())
print("Postorder traversal:", binary_search_tree.postorder_traversal())

print()

class FreeSpaceBinarySearchTree: # binary search tree, free space list
    def __init__(self, size):
        self.data = [None] * size
        self.left = [-1] * size
        self.right = [-1] * size
        self.pointer = [i for i in range(1, size)] + [-1]
        self.root = -1
        self.next_free = 0

    def insert(self, data): # edit data --> edit pointer
        if self.next_free == -1:
            print(f"Binary search tree is full! Data not entered: {data}")
        elif self.root == -1:
            self.data[self.next_free] = data
            self.pointer[self.next_free], self.root, self.next_free = -1, self.next_free, self.pointer[self.next_free]
        else:
            curr_pointer = self.root
            while curr_pointer != -1:
                if data < self.data[curr_pointer]:
                    if self.left[curr_pointer] == -1:
                        self.data[self.next_free] = data
                        self.pointer[self.next_free], self.left[curr_pointer], self.next_free = -1, self.next_free, self.pointer[self.next_free]
                        curr_pointer = -1
                    else:
                        curr_pointer = self.left[curr_pointer]
                else:
                    if self.right[curr_pointer] == -1:
                        self.data[self.next_free] = data
                        self.pointer[self.next_free], self.right[curr_pointer], self.next_free = -1, self.next_free, self.pointer[self.next_free]
                        curr_pointer = -1
                    else:
                        curr_pointer = self.right[curr_pointer]

    def search(self, data):
        curr_pointer = self.root
        while curr_pointer != -1 and data != self.data[curr_pointer]:
            if data < self.data[curr_pointer]:
                curr_pointer = self.left[curr_pointer]
            else:
                curr_pointer = self.right[curr_pointer]
        if data == self.data[curr_pointer]: # item found in binary search tree
            return True
        else: # item not found in binary search tree
            return False
        
    def height(self):
        def helper(self, curr_pointer):
            if curr_pointer == -1:
                return -1
            else:
                return 1 + max(helper(self, self.left[curr_pointer]), helper(self, self.right[curr_pointer]))
        return helper(self, self.root)

    def inorder_traversal(self): # left, display, right
        def helper(self, curr_pointer):
            if curr_pointer == -1:
                return []
            else:
                return helper(self, self.left[curr_pointer]) + [self.data[curr_pointer]] + helper(self, self.right[curr_pointer])
        def helper2(self, curr_pointer):
            if curr_pointer != -1:
                if self.left[curr_pointer] != -1:
                    helper2(self, self.left[curr_pointer])
                    
                print(self.data[curr_pointer])

                if self.right[curr_pointer] != -1:
                    helper2(self, self.right[curr_pointer])
        helper2(self, self.root)
        return helper(self, self.root)

    def preorder_traversal(self): # display, left, right
        def helper(self, curr_pointer):
            if curr_pointer == -1:
                return []
            else:
                return [self.data[curr_pointer]] + helper(self, self.left[curr_pointer]) + helper(self, self.right[curr_pointer])
        def helper2(self, curr_pointer):
            if curr_pointer != -1:
                print(self.data[curr_pointer])
                
                if self.left[curr_pointer] != -1:
                    helper2(self, self.left[curr_pointer])

                if self.right[curr_pointer] != -1:
                    helper2(self, self.right[curr_pointer])
        helper2(self, self.root)
        return helper(self, self.root)

    def postorder_traversal(self): # left, right, display
        def helper(self, curr_pointer):
            if curr_pointer == -1:
                return []
            else:
                return helper(self, self.left[curr_pointer]) + helper(self, self.right[curr_pointer]) + [self.data[curr_pointer]]
        def helper2(self, curr_pointer):
            if curr_pointer != -1:
                if self.left[curr_pointer] != -1:
                    helper2(self, self.left[curr_pointer])

                if self.right[curr_pointer] != -1:
                    helper2(self, self.right[curr_pointer])
                    
                print(self.data[curr_pointer])
        helper2(self, self.root)
        return helper(self, self.root)

free_space_binary_search_tree = FreeSpaceBinarySearchTree(len(lst))

for item in lst:
    free_space_binary_search_tree.insert(item)

print(f"Search for {lst[0]}:", free_space_binary_search_tree.search(lst[0]))
print(f"Search for 0:", free_space_binary_search_tree.search(0))

print("Height of free space binary search tree:", free_space_binary_search_tree.height())

print("Inorder traversal:", free_space_binary_search_tree.inorder_traversal())
print("Preorder traversal:", free_space_binary_search_tree.preorder_traversal())
print("Postorder traversal:", free_space_binary_search_tree.postorder_traversal())

print()
