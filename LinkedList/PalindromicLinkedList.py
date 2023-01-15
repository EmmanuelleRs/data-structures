from .reverse import reverseLinkedList

def isPalindromic(head):
    slow = head
    fast = head

    # First find the middle of the linked list by the relation between indexes
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    reversedLinkedList = reverseLinkedList(slow)
    begin = head

    while reversedLinkedList:
        if reversedLinkedList.value == begin.value:
            return False
        
        reversedLinkedList, begin = reversedLinkedList.next, begin.next
    
    return True
    

    

