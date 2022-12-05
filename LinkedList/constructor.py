class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def set_head(self, nodeToInsert):
        if self.head is None:
            self.head = nodeToInsert
            self.tail = nodeToInsert
            return
        self.insert_before(self.head, nodeToInsert)
    
    def set_tail(self, nodeToInsert):
        if self.tail is None:
            self.set_head(nodeToInsert)
            return
        self.insert_after(self.tail, nodeToInsert)
        
    def insert_before(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
    
    def insert_after(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
    
    def insert_at_position(self, position, nodeToInsert):
        if position == 1:
            self.set_head(nodeToInsert)
            return
        
        currentNode = self.head
        currentPosition = 1

        while currentNode is not None and currentPosition != position:
            currentNode = currentNode.next
            currentPosition += 1
        
        if currentNode is not None:
            self.insert_before(currentNode, nodeToInsert)
        else:
            self.set_tail(nodeToInsert)



