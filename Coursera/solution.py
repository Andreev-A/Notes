from sys import stdin


class MatrixError(BaseException):
    def __init__(self, cls, other):
        self.matrix1 = cls
        self.matrix2 = other


class Matrix:
    def __init__(self, cls):
        self.cls = [lst[:] for lst in cls]

    def __str__(self):
        s = ''
        for i in self.cls:
            if s:
                s += '\n'
            s += '\t'.join(map(str, i))
        return s

    def __add__(self, other):
        if len(self.cls) == len(other.cls):
            return Matrix(
                [[num + other.cls[j][i] for i, num in enumerate(number)]
                 for j, number in enumerate(self.cls)])

        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        return Matrix([[num * other for num in number]
                       for number in self.cls])

    __rmul__ = __mul__

    def size(self):
        return len(self.cls), len(self.cls[0])

    def transpose(self):
        if isinstance(self, Matrix):
            self.cls = [*zip(*self.cls)]
            return Matrix(self.cls)

    @staticmethod
    def transposed(cls):
        return Matrix([*zip(*cls.cls)])


exec(stdin.read())
