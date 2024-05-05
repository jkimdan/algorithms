import random
import string
import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{repr(self.item[0])}: {repr(self.item[1])}"

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.list_size = 0

    def add_node(self, node, side="front"):
        if side not in ["front", "back"]:
            raise ValueError("Invalid side! Must be 'front' or 'back'")
        
        if self.list_size == 0:
            self.first = self.last = node
        else:
            if side == "front":
                node.next = self.first
                self.first.prev = node
                self.first = node
            elif side == "back":
                node.prev = self.last
                self.last.next = node
                self.last = node

        self.list_size += 1
        
    def delete_node(self, index):
        if index >= self.list_size or self.first == None:
            raise IndexError("Linked List index out of range.")
        current = self.first
        for i in range(index):
            current = current.next
        
        # edge cases: head, last, middle
        if current.prev:
            current.prev.next = current.next
        else: # head case
            self.first = current.next

        if current.next: 
            current.next.prev = current.prev
        else: # tail case
            self.last = current.prev
        
        self.list_size -= 1

    def __str__(self):
        elements = []
        current = self.first
        while current:
            elements.append(str(current))
            current = current.next
        return ', '.join(elements)
    
class HashTable_NoScaling:
    def __init__(self):
        self.m = 10
        self.table = [LinkedList() for _ in range(self.m)]
        self.n = 0
        self.load_factor = self.n / self.m
        self.order = [] # added to preserve order of insertion
    
    def __hash(self, key):
        pre_hash = hash(key)
        return pre_hash % self.m
    
    def __setitem__(self, key, value):
        index = self.__hash(key)
        current = self.table[index].first 
        while current:
            if current.item[0] == key:
                current.item = (key, value)
                return
            current = current.next
        self.table[index].add_node(Node((key, value)), side="back")
        self.n += 1
        self.order.append(key)

    def __getitem__(self, key):
        index = self.__hash(key)
        current = self.table[index].first
        while current:
            if current.item[0] == key:
                return current.item[1]
            current = current.next
        raise KeyError("Key not found")
    
    def __delitem__(self, key):
        index = self.__hash(key)
        collisions = self.table[index]
        node = 0
        current = collisions.first
        while current: 
            if current.item[0] == key:
                collisions.delete_node(node)
                self.n -= 1
                self.order.remove(key)
                return
            current = current.next
            node += 1
        raise KeyError("Key not found")

    def __str__(self):
        if self.n == 0:
            return "{}"
        built = []
        for key in self.order:
            try:
                value = self[key]
                built.append(f"{repr(key)}: {repr(value)}")
            except KeyError:
                continue
        return '{' + ', '.join(built) + '}'

class HashTable:
    def __init__(self):
        self.m = 10
        self.table = [LinkedList() for _ in range(self.m)]
        self.n = 0
        self.load_factor = self.n / self.m
        self.order = [] # added to preserve order of insertion
    
    def __hash(self, key):
        pre_hash = hash(key)
        return pre_hash % self.m
    
    def __table_double(self):
        old_nodes = self.table
        self.m *= 2
        self.table = [LinkedList() for _ in range(self.m)]
        self.order = []
        self.n = 0
        for val in old_nodes:
            current = val.first
            while current:
                self.__setitem__(current.item[0], current.item[1])
                current = current.next

    def __setitem__(self, key, value):
        self.load_factor = self.n / self.m
        if self.load_factor > 0.7:
            self.__table_double()
        
        index = self.__hash(key)
        current = self.table[index].first 
        while current:
            if current.item[0] == key:
                current.item = (key, value)
                return
            current = current.next
        self.table[index].add_node(Node((key, value)), side="back")
        self.n += 1
        self.order.append(key)

    def __getitem__(self, key):
        index = self.__hash(key)
        current = self.table[index].first
        while current:
            if current.item[0] == key:
                return current.item[1]
            current = current.next
        raise KeyError("Key not found")
    
    def __delitem__(self, key):
        index = self.__hash(key)
        collisions = self.table[index]
        node = 0
        current = collisions.first
        while current: 
            if current.item[0] == key:
                collisions.delete_node(node)
                self.n -= 1
                self.order.remove(key)
                self.load_factor = self.n / self.m
                return
            current = current.next
            node += 1
        raise KeyError("Key not found")

    def __str__(self):
        if self.n == 0:
            return "{}"
        built = []
        for key in self.order:
            try:
                value = self[key]
                built.append(f"{repr(key)}: {repr(value)}")
            except KeyError:
                continue
        return '{' + ', '.join(built) + '}'

def make_junk_items(amount):
    random_items = []
    for i in range(amount):
        length = random.randint(1,20)
        key = ""
        for _ in range(length):
            key += random.choice(string.ascii_letters)
        value = random.randint(0,100)
        random_items.append((key, value))
    return random_items

random_items = make_junk_items(5000)
static_table = HashTable_NoScaling()
dynamic_table = HashTable()

avg_static_times = []
avg_dynamic_times = [] 
included_keys = []

for n in range(5000):
    key, value = random.choice(random_items)
    included_keys.append(key)
    static_table[key] = value
    dynamic_table[key] = value
    if n % 10 == 0:
        static_times = []
        dynamic_times = []
        for i in range(100):
            search_key = random.choice(included_keys)
            start1 = perf_counter()
            _ = static_table[search_key]
            end1 = perf_counter()
            static_times.append(end1 - start1)

            start2 = perf_counter()
            _ = dynamic_table[search_key]
            end2 = perf_counter()
            dynamic_times.append(end2 -  start2)

        avg_static_times.append(np.mean(static_times))
        avg_dynamic_times.append(np.mean(dynamic_times))


plt.figure(figsize=(10, 5))
plt.plot(avg_dynamic_times, label='Scaling Hash Table')
plt.plot(avg_static_times, label='Non-Scaling Hash Table')
plt.xlabel('Insertion Batches (x10)')
plt.ylabel('Average Search Time (seconds)')
plt.title('Hash Table Performance Comparison')
plt.legend()
plt.grid(True)
plt.show()