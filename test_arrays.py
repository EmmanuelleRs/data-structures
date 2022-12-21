from Arrays.firstduplicate import first_duplicate

def test_first_duplicate():
    assert first_duplicate([1, 1, 2, 3, 4, 5, 5]) == 1
    assert first_duplicate([1, 2, 2, 3, 4, 5, 5]) == 2
    assert first_duplicate([1, 2, 3, 3, 4, 5, 5]) == 3
    assert first_duplicate([1, 2, 3, 4, 4, 5, 5]) == 4
    assert first_duplicate([1, 2, 3, 4, 5, 5, 5]) == 5
