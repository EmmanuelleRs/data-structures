def reverseLinkedList(linkedList):
    # Current node depends on the linkedList Constructor, in this case,
    # please check the LinkedList.constructor module

    # 1 - 2 - 3 - 4

    prevNode, currentNode = None, linkedList.head

    while currentNode:
        tempNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = tempNode
    
    return prevNode
        
