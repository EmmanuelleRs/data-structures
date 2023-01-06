from BinarySearch.recursion import binarySearch

def test_binary():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binarySearch(array, 1) == 0
    assert binarySearch(array, 2) == 1
    assert binarySearch(array, 3) == 2
    assert binarySearch(array, 4) == 3
    assert binarySearch(array, 5) == 4
    assert binarySearch(array, 6) == 5
    assert binarySearch(array, 7) == 6
    assert binarySearch(array, 8) == 7
    assert binarySearch(array, 9) == 8