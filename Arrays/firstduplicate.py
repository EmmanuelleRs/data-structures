def first_duplicate(array):
    count = {}

    for num in array:
        if num not in count:
            count[num] = 0
        count[num] += 1

        if count[num] >= 2:
            return num
        
    return -1
