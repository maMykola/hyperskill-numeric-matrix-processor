from matrix import Matrix


class MatrixSystem:
    STATE_OFF = "off"
    STATE_MAIN = "main"
    STATE_TRANSPOSE = "transpose"

    ACTION_EXIT = "0"
    ACTION_ADD = "1"
    ACTION_MULTIPLY_BY_CONSTANT = "2"
    ACTION_MULTIPLY_MATRICES = "3"
    ACTION_TRANSPOSE = "4"
    ACTION_DETERMINANT = "5"
    ACTION_INVERSE = "6"

    ACTION_MAIN_DIAGONAL = "1"
    ACTION_SIDE_DIAGONAL = "2"
    ACTION_VERTICAL_LINE = "3"
    ACTION_HORIZONTAL_LINE = "4"

    TRANSPOSE_ACTIONS = (
        ACTION_MAIN_DIAGONAL,
        ACTION_SIDE_DIAGONAL,
        ACTION_VERTICAL_LINE,
        ACTION_HORIZONTAL_LINE
    )

    DIRECTION_MAP = {
        ACTION_MAIN_DIAGONAL: Matrix.TRANSPOSE_MAIN,
        ACTION_SIDE_DIAGONAL: Matrix.TRANSPOSE_SIDE,
        ACTION_VERTICAL_LINE: Matrix.TRANSPOSE_VERTICAL,
        ACTION_HORIZONTAL_LINE: Matrix.TRANSPOSE_HORIZONTAL
    }

    def __init__(self):
        self.state = self.STATE_MAIN

    def run(self):
        while self.state != self.STATE_OFF:
            self.display_actions()
            self.do(input('Your choice: '))

    def display_actions(self):
        if self.state == self.STATE_MAIN:
            print("1. Add matrices")
            print("2. Multiply matrix by a constant")
            print("3. Multiply matrices")
            print("4. Transpose matrix")
            print("5. Calculate a determinant")
            print("6. Inverse matrix")
            print("0. Exit")
        elif self.state == self.STATE_TRANSPOSE:
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")

    def do(self, action):
        if self.state == self.STATE_MAIN:
            self.do_main(action)
        elif self.state == self.STATE_TRANSPOSE:
            self.do_transpose(action)

    def do_main(self, action):
        if action == self.ACTION_EXIT:
            self.state = self.STATE_OFF
        elif action == self.ACTION_ADD:
            self.add_action()
        elif action == self.ACTION_MULTIPLY_BY_CONSTANT:
            self.multiply_constant_action()
        elif action == self.ACTION_MULTIPLY_MATRICES:
            self.multiply_matrices_action()
        elif action == self.ACTION_TRANSPOSE:
            self.state = self.STATE_TRANSPOSE
        elif action == self.ACTION_DETERMINANT:
            self.find_determinant()
        elif action == self.ACTION_INVERSE:
            self.inverse()
        else:
            print("Unknown action")

    def do_transpose(self, action):
        if action in self.TRANSPOSE_ACTIONS:
            self.display_result(self.get_matrix().transpose(self.DIRECTION_MAP[action]))
        else:
            print("Unknown action")

        self.state = self.STATE_MAIN

    def add_action(self):
        m1 = self.get_matrix('first matrix')
        m2 = self.get_matrix('second matrix')
        self.display_result(m1.add(m2))

    def multiply_constant_action(self):
        m = self.get_matrix()
        number = float(input('Enter constant: '))
        self.display_result(m.mul_const(number))

    def multiply_matrices_action(self):
        m1 = self.get_matrix('first matrix')
        m2 = self.get_matrix('second matrix')
        self.display_result(m1.mul(m2))

    def find_determinant(self):
        self.display_result(self.get_matrix().determinant())

    def inverse(self):
        result = self.get_matrix().inverse()
        if result is None:
            print("This matrix doesn't have an inverse.")
        else:
            self.display_result(result)

    @staticmethod
    def display_result(result):
        if result is None:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            print(result)

    @staticmethod
    def get_matrix(message='matrix'):
        rows, cols = [int(x) for x in input(f"Enter size of {message}: ").split()]
        print(f"Enter {message}:")
        return Matrix.create_by_input(rows, cols)


ms = MatrixSystem()
ms.run()
