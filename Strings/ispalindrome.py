def isPalindrome(string):
    left = 0
    rigth = len(string) - 1

    while left < rigth:
        if string[left] != string[rigth]:
            return False
    
    return False