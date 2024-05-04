
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.item[0]}: {self.item[1]}"

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.list_size = 0

    # fix this structure
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
        return '{' + ', '.join(elements) + '}'

node1 = Node((0,1))
node2 = Node((1,5))
node3 = Node((2, 1234))
linked_list = LinkedList()
linked_list.add_node(node1)
linked_list.add_node(node2)
linked_list.add_node(node3)
print(linked_list)
linked_list.delete_node(1)
print(linked_list)