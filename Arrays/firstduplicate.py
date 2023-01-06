
# O(n) time complexity since the array neads to be traversed al most once in case there's not duplicates in the array.
# O(1) space complexity since were are storing just one dictionary to track the duplicate elements

class FindFirstDuplicate():
    def __init__(self, array: list):
        self.array = array
    
    def using_dictionarie(self) -> -1:
        """Find the first duplicate element into an array,
        using a dictionarie.

        Args:
            array: This is the list of integer where the algorith will search
            the first duplicate element.

        Returns:
            int: return the firs duplicate element,
            otherwise return -1
        """

        count = {}

        for num in self.array:
            if num not in count:
                count[num] = 0
            count[num] += 1

            if count[num] >= 2:
                return num
            
        return -1
    
    def using_set(self) -> -1:
        this_set = set()

        for element in self.array:
            if element in this_set:
                return element
            this_set.add(element)
            
        return -1