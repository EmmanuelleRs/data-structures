
def RotateMatrix():
    def __init__(self, matrix) -> list:
        self.matrix = matrix

    def clockwise(self):
        l, r = 0, len(self.matrix)

        while l < r:
            for i in range(r - l): # -> range(l, r)
                top, bottom = l, r # -> since this is  a square matrix

                topLeft = self.matrix[top][l]

                self.matrix[top][l + i] = self.matrix[bottom - i][l]
                
                self.matrix[bottom - i][l] = self.matrix[bottom][r - i]

                self.matrix[bottom][r - 1] = self.matrix[top + i][r]

                self.matrix[top + i][r] = topLeft
        
        return self.matrix
    