from LinkedList.constructor import Node, DoublyLinkedList

# 1 - 2 - 3 - 4 - 5
Node0 = Node(0)
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

linked_list = DoublyLinkedList()

linked_list.set_head(Node0)
linked_list.insert_after(Node0, Node1)
linked_list.insert_after(Node1, Node2)
linked_list.insert_after(Node2, Node3)
linked_list.insert_after(Node3, Node4)
linked_list.insert_after(Node4, Node5)



def remove_k(linked_list, k):
    current_node = linked_list.head
    current_idx = 1

    while current_idx < k and current_node.value:
        current_node = current_node.next
        current_idx += 1
    

    if current_node is not None:
        current_node.next = current_node.next.next
        current_node.next.prev = current_node
    

remove_k(linked_list=linked_list, k=0)

print(Node1.next.value)
print(Node3.prev.value)


