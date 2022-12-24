def binarySearch(array, target):
    return subBinarySearch(array, target, 0, len(array) - 1)
    
def subBinarySearch(array, target, left, right):
    if left > right:
        return -1
    
    pottentialMatch = array[(mid := (left + right) // 2)]

    if target == pottentialMatch:
        return mid
    elif target < pottentialMatch:
        return subBinarySearch(array, target, left, mid - 1)
    else:
        return subBinarySearch(array, target, mid + 1, right)
        