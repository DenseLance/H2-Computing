from random import randint

keys = [randint(1, 100) for _ in range(10)]
data = [randint(1, 100) for _ in range(10)]

print("Keys:", keys)
print("Data:", data)

class HashTable:
    def __init__(self, size):
        self.slots = [None] * size
        self.data = [None] * size
        self.count = 0
        self.size = size

    def hash_function(self, key):
        return key % self.size

    def rehash(self, hash_value): # linear probe
        return (hash_value + 1) % self.size

    def insert(self, key, data):
        if self.load_factor() == 1:
            print("Hash table is full! Key not entered:", key)
        else:
            hash_value = self.hash_function(key)
            while self.slots[hash_value] and self.slots[hash_value] != key: # rehash if there is collision
                hash_value = self.rehash(hash_value)
            if self.slots[hash_value] == key: # key already exists in hash table
                print(f"Key {key} already exists in hash table!")
            else:
                self.slots[hash_value] = key
                self.data[hash_value] = data
                self.count += 1

    def search(self, key): # search by key
        hash_value = self.hash_function(key)
        count = 0
        while self.slots[hash_value] and self.slots[hash_value] != key and count < self.size:
            hash_value = self.rehash(hash_value)
            count += 1
        if self.slots[hash_value] == key:
            return self.data[hash_value]
    
    def load_factor(self):
        return self.count / self.size

hash_table = HashTable(len(keys) - 1)

for i in range(len(keys)):
    hash_table.insert(keys[i], data[i])

for key in keys:
    print(hash_table.search(key))
