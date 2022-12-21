
class Array():
    def __init__(self, array):
        self.array = array
    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
    # o(n*n) time complexity
    def bubble(self):
        for i in range(len(self.array)):
            for j in range(i, len(self.array)):
                if self.array[i] > self.array[j]:
                    self.swap(i, j)
        return self.array
    def insertion(self):
        for i in range(1, len(self.array)):
            j = i
            while j > 0 and self.array[j] < self.array[j - 1]:
                self.swap(j , j - 1)
                j -= 1
        return self.array
    def selection(self):
        currentIdx = 0
        while currentIdx < len(self.array) - 1:
            smallestIdx = currentIdx
            for i in range(currentIdx + 1, len(self.array)):
                if self.array[smallestIdx] > self.array[i]:
                    smallestIdx = i
            self.swap(currentIdx, smallestIdx)
            currentIdx += 1
        return self.array







