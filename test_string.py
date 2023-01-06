from Strings.validIPAddresses import solution

def test_validIPAddresses():
    array_solution = solution('1921680')

    assert '1.9.216.80' in array_solution
    assert '1.92.16.80' in array_solution
    assert '1.9.21.680' not in array_solution
    assert '1.9.2168.0' not in array_solution
    assert '19.92.16.680' not in array_solution