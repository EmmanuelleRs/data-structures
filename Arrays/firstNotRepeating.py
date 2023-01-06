
# O(n) Time complexity since the array needs to be transversed twice O(2n) -> O(n)
# O(1) Space Complexity since we are storing each element on a single dictionarie

class FirstNotRepeating():
    def __init__(self, array) -> None:
        self.array = array

    def find(self):
        count = {}

        for element in self.array:
            if element not in count:
                count[element] = 0
            count[element] += 1

        for element in count:
            if count[element] == 1:
                return element
            
        return None
            
    