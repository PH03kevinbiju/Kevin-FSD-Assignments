class MinMax:
    def __init__(self, min1, max1, state):
        self.max1 = max1
        self.min1 = min1
        self.state = state

    def matrix(self):
        m1 = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
        print("matrix m1:")
        print(m1)
        return m1

    def checkbest(self, m2):
        count = 0
        for i in range(3):
            for j in range(3):
                if i<2 and j<2:
                     if (m2[i][j] == 0 and
                        m2[i+1][j] == 0 and
                        m2[i+2][j] == 0):
                        count += 1
                        break
        print(count)

    def max(self, m2):
        for i in range(3):
            for j in range(3):
                if m2[i][j] == '0':l
                    m2[i][j] = '1'
        print("matrix after max operation:")
        print(m2)
        return m2

# Example usage
a = MinMax("", "", "")
matrix = a.matrix()
a.checkbest(matrix)
updated_matrix = a.max(matrix)
