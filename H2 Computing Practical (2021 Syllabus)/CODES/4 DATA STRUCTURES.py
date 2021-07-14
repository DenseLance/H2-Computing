from random import randint, shuffle

lst = [18, 87, 88, 72, 31, 33, 73, 55, 97, 63]

print("List:", lst)
print()

class Stack: # LIFO
    def __init__(self):
        self.stack = [] # end of stack is first item

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self): # peek at first item
        if self.stack:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

stack = Stack()

for item in lst:
    stack.push(item)

for _ in range(len(lst)):
    print("Item popped from stack:", stack.pop())

print("Size of stack after popping:", stack.size())

print()

class Queue: # FIFO
    def __init__(self):
        self.queue = [] # end of queue is first item

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

    def peek(self): # peek at last item
        if self.queue:
            return self.queue[0]

    def size(self):
        return len(self.queue)
        
queue = Queue()

for item in lst:
    queue.enqueue(item)

for _ in range(len(lst)):
    print("Item dequeued from queue:", queue.dequeue())

print("Size of queue after dequeuing:", queue.size())

print()

class CircularQueue: # FIFO
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
        self.count = 0
        self.max_size = max_size

    def enqueue(self, data):
        if self.count == self.max_size:
            print(f"Circular queue is full! Data not enqueued: {data}")
        else:
            self.queue[self.tail] = data
            self.tail = (self.tail + 1) % self.max_size
            self.count += 1

    def dequeue(self):
        if self.count == 0:
            print(f"Circular queue is empty! Data not dequeued: {data}")
        else:
            data = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.count -= 1
            return data

    def peek(self): # peek at last item
        return self.queue[self.head]
                    
    def size(self):
        return self.count

circular_queue = CircularQueue(len(lst))

for item in lst:
    circular_queue.enqueue(item)

for _ in range(len(lst)):
    print("Item dequeued from circular queue:", circular_queue.dequeue())

print("Size of circular queue after dequeuing:", circular_queue.size())

print()

class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

class LinkedList: # sorted linked list, OOP
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            if data <= self.head.get_data(): # item at start of linked list
                self.head = Node(data, self.head)
            else:
                curr_node = self.head
                prev_node = None
                while curr_node and data > curr_node.get_data():
                    prev_node = curr_node
                    curr_node = curr_node.get_next()
                prev_node.set_next(Node(data, curr_node)) # item in middle/at end of linked list

    def delete(self, data):
        if self.head == None:
            print("Data not found in linked list.")
        else:
            if data == self.head.get_data(): # item at start of linked list
                self.head = self.head.get_next()
            else:
                curr_node = self.head
                prev_node = None
                while curr_node and data > curr_node.get_data():
                    prev_node = curr_node
                    curr_node = curr_node.get_next()
                if curr_node and data == curr_node.get_data(): # item in middle/at end of linked list
                    prev_node.set_next(curr_node.get_next())
                else:
                    print("Data not found in linked list.")
                
    def search(self, data):
        curr_node = self.head
        while curr_node and data > curr_node.get_data():
            curr_node = curr_node.get_next()
        if curr_node and data == curr_node.get_data(): # item found in linked list
            return True
        else: # item not found in linked list
            return False

    def size(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.get_next()
        return count

    def return_as_list(self):
        result = []
        curr_node = self.head
        while curr_node:
            result.append(curr_node.get_data())
            curr_node = curr_node.get_next()
        return result

linked_list = LinkedList()

for item in lst:
    linked_list.insert(item)

temp = lst.copy()
temp.sort()
print("Linked list is sorted:", linked_list.return_as_list() == temp)

temp = lst.copy()
shuffle(temp)

for item in temp[:5]:
    linked_list.delete(item)
    print("Item deleted from linked list:", item)

print(f"Search for {temp[0]}:", linked_list.search(temp[0]))
print(f"Search for {temp[5]}:", linked_list.search(temp[5]))

print("Size of linked list after deleting:", linked_list.size())

print("Linked list:", linked_list.return_as_list())

print()

class FreeSpaceLinkedList: # sorted linked list, free space list
    def __init__(self, size):
        self.data = [None] * size
        self.pointer = [i for i in range(1, size)] + [-1]
        self.head = -1
        self.next_free = 0

    def insert(self, data): # edit data --> edit pointer
        if self.next_free == -1:
            print(f"Linked list is full! Data not entered: {data}")
        elif self.head == -1:
            self.data[self.next_free] = data
            self.pointer[self.next_free], self.head, self.next_free = -1, self.next_free, self.pointer[self.next_free]
        else:
            if data <= self.data[self.head]: # item at start of linked list
                self.data[self.next_free] = data
                self.pointer[self.next_free], self.head, self.next_free = self.head, self.next_free, self.pointer[self.next_free]
            else:
                curr_pointer = self.head
                prev_pointer = -1
                while curr_pointer != -1 and data > self.data[curr_pointer]:
                    prev_pointer = curr_pointer
                    curr_pointer = self.pointer[curr_pointer]
                if curr_pointer != -1: # item in middle of linked list
                    self.data[self.next_free] = data
                    self.pointer[self.next_free], self.pointer[prev_pointer], self.next_free = self.pointer[prev_pointer], self.next_free, self.pointer[self.next_free]
                else: # item at end of linked list
                    self.data[self.next_free] = data
                    self.pointer[self.next_free], self.pointer[prev_pointer], self.next_free = -1, self.next_free, self.pointer[self.next_free]

    def delete(self, data): # edit data --> edit pointer
        if self.head == -1:
            print("Data not found in linked list.")
        else:
            if data == self.data[self.head]: # item at start of linked list
                self.data[self.head] = None
                self.pointer[self.head], self.head, self.next_free = self.next_free, self.pointer[self.head], self.head
            else:
                curr_pointer = self.head
                prev_pointer = -1
                while curr_pointer != -1 and data > self.data[curr_pointer]:
                    prev_pointer = curr_pointer
                    curr_pointer = self.pointer[curr_pointer]
                if curr_pointer != -1 and data == self.data[curr_pointer]: # item in middle/at end of linked list
                    self.data[curr_pointer] = None
                    self.pointer[curr_pointer], self.pointer[prev_pointer], self.next_free = self.next_free, self.pointer[curr_pointer], curr_pointer
                else: # item not found in linked list
                    print("Data not found in linked list.")

    def search(self, data):
        curr_pointer = self.head
        while curr_pointer != -1 and data > self.data[curr_pointer]:
            curr_pointer = self.pointer[curr_pointer]
        if data == self.data[curr_pointer]: # item found in linked list
            return True
        else: # item not found in linked list
            return False

    def size(self):
        count = 0
        curr_pointer = self.head
        while curr_pointer != -1:
            count += 1
            curr_pointer = self.pointer[curr_pointer]
        return count
    
    def return_as_list(self):
        result = []
        curr_pointer = self.head
        while curr_pointer != -1:
            result.append(self.data[curr_pointer])
            curr_pointer = self.pointer[curr_pointer]
        return result

free_space_linked_list = FreeSpaceLinkedList(len(lst))

for item in lst:
    free_space_linked_list.insert(item)

temp = lst.copy()
temp.sort()
print("Free space linked list is sorted:", free_space_linked_list.return_as_list() == temp)

temp = lst.copy()
shuffle(temp)

for item in temp[:5]:
    free_space_linked_list.delete(item)
    print("Item deleted from free space linked list:", item)

print(f"Search for {temp[0]}:", free_space_linked_list.search(temp[0]))
print(f"Search for {temp[5]}:", free_space_linked_list.search(temp[5]))

print("Size of free space linked list after deleting:", free_space_linked_list.size())

print("Free space linked list:", free_space_linked_list.return_as_list())

print()
