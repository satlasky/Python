class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
        res = ""
        for i in range(self.rows):
            for j in range(self.cols):
                res += str(self.matrix[i][j]) + " "
            res += "\n"
        return res

    def add(self, m):
        if self.rows != m.rows or self.cols != m.cols:
            raise ValueError("Матрицы не имеют одинаковый размер.")
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                res.matrix[i][j] = self.matrix[i][j] + m.matrix[i][j]
        return res

    def subtract(self, m):
        if self.rows != m.rows or self.cols != m.cols:
            raise ValueError("Матрицы не имеют одинаковый размер.")
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                res.matrix[i][j] = self.matrix[i][j] - m.matrix[i][j]
        return res

m1 = Matrix(2, 2)
m1.matrix = [[1, 2], [3, 4]]
m2 = Matrix(2, 2)
m2.matrix = [[5, 6], [7, 8]]
print(m1.add(m2))
print(m1.subtract(m2))