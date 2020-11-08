class Matrix:
    TRANSPOSE_MAIN = "main"
    TRANSPOSE_SIDE = "side"
    TRANSPOSE_VERTICAL = "vertical"
    TRANSPOSE_HORIZONTAL = "horizontal"

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[0] * cols for _ in range(rows)]

    @staticmethod
    def create_by_input(rows, cols):
        matrix = Matrix(rows, cols)
        matrix.cells = [[Matrix.convert(float(x)) for x in input().split()] for _ in range(rows)]
        return matrix

    @staticmethod
    def convert(number):
        return int(number) if float(number).is_integer() else number

    def add(self, matrix):
        if matrix.rows != self.rows or matrix.cols != self.cols:
            return None

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.cells[i][j] = self.convert(self.cells[i][j] + matrix.cells[i][j])

        return result

    def mul_const(self, number):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.cells[i][j] = self.convert(self.cells[i][j] * number)
        return result

    def mul(self, matrix):
        if self.cols != matrix.rows:
            return None

        result = Matrix(self.rows, matrix.cols)
        for i in range(self.rows):
            for j in range(matrix.cols):
                result.cells[i][j] = self.convert(self.get_product(matrix, i, j))

        return result

    def transpose(self, direction):
        if direction == self.TRANSPOSE_MAIN:
            return self.transpose_main()
        elif direction == self.TRANSPOSE_SIDE:
            return self.transpose_side()
        elif direction == self.TRANSPOSE_VERTICAL:
            return self.transpose_vertical()
        elif direction == self.TRANSPOSE_HORIZONTAL:
            return self.transpose_horizontal()
        else:
            return None

    def transpose_main(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.cells[j][i] = self.cells[i][j]
        return result

    def transpose_side(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.cells[j][i] = self.cells[self.rows - i - 1][self.cols - j - 1]
        return result

    def transpose_vertical(self):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.cells[i][j] = self.cells[i][self.cols - j - 1]
        return result

    def transpose_horizontal(self):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.cells[i][j] = self.cells[self.rows - i - 1][j]
        return result

    def determinant(self):
        if self.rows != self.cols:
            return None
        elif self.rows == 2:
            return self.cells[0][0] * self.cells[1][1] - self.cells[1][0] * self.cells[0][1]
        elif self.rows == 1:
            return self.cells[0][0]

        determinant = 0
        for i in range(self.cols):
            minor = self.minor(0, i)
            determinant += (-1) ** i * self.cells[0][i] * minor.determinant()

        return determinant

    def inverse(self):
        dt = self.determinant()
        if dt == 0:
            return None
        else:
            return self.cofactor().transpose_main().mul_const(1 / dt)

    def cofactor(self):
        matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                matrix.cells[i][j] = (-1) ** (i + j) * self.minor(i, j).determinant()
        return matrix

    def minor(self, row, col):
        matrix = Matrix(self.rows - 1, self.cols - 1)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                matrix.cells[i][j] = self.cells[i if i < row else i + 1][j if j < col else j + 1]
        return matrix

    def get_product(self, matrix, row, col):
        value = 0
        for i in range(self.cols):
            value += self.cells[row][i] * matrix.cells[i][col]
        return value

    def __str__(self):
        return "\n".join([" ".join([str(x) for x in line]) for line in self.cells])
