from LinkedList.constructor import Node, DoublyLinkedList

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

linkedList = DoublyLinkedList()

linkedList.set_head(node_1)
linkedList.set_tail(node_2)

def test_linkedList():
    assert linkedList.head.value == 1
    assert linkedList.tail.value == 2

def test_insertAfter():
    linkedList.insert_after(node_1, node_3)
    assert linkedList.head.next.value == 3
    assert linkedList.tail.value == 2
    assert linkedList.tail.prev.value == 3
    assert linkedList.tail.prev.value == 1