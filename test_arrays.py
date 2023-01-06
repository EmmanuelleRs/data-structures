from Arrays.firstduplicate import FindFirstDuplicate
from Arrays.firstNotRepeating import FirstNotRepeating

def test_first_duplicate():
    first_duplicate_1 = FindFirstDuplicate(array=[1, 1, 2, 3, 4, 5, 5])
    first_duplicate_2 = FindFirstDuplicate(array=[1, 2, 3, 4, 4, 5, 5])

    assert first_duplicate_1.using_dictionarie() == first_duplicate_1.using_set()
    assert first_duplicate_1.using_dictionarie() != first_duplicate_2.using_set()
    assert first_duplicate_2.using_dictionarie() == first_duplicate_2.using_set()
    assert first_duplicate_1.using_dictionarie() == 1
    assert first_duplicate_2.using_dictionarie() != 1
    assert first_duplicate_2.using_dictionarie() == 4
    assert first_duplicate_1.using_set() == 1

def test_fistNotRepeating():
    solution = FirstNotRepeating([1, 3, 4, 1, 3, 4, 5, 1, 4, 9, 2, 0])

    assert solution.find() == 5
