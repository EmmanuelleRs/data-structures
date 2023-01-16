
# [3, 3, 4, 5, 6, 2, 1, 1, 2, 3]
# toMove = 3

def moveToEnd(array, toMove):
    start = 0
    end = len(array) - 1

    while start < end:
        if array[start] == toMove and array[end] != toMove:
            swap(array, start, end)
        elif array[start] == toMove and array[end] == toMove:
            end -= 1
        else:
            start += 1

    return array

def swap(array, start, end):
    array[start], array[end] = array[end], array[start]
