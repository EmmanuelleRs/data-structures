from Recursion.fibonacchi import dinamyc

def test_fibonacci():
    assert dinamyc(1) == 1
    assert dinamyc(2) == 1
    assert dinamyc(3) == 2
    assert dinamyc(4) == 3
    assert dinamyc(5) == 5
    assert dinamyc(6) == 8
    assert dinamyc(60) == 1548008755920
    assert dinamyc(100) == 354224848179261915075
