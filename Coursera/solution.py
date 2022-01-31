from sys import stdin


class Matrix:
    def __init__(self, lst):
        self.my_list = lst[:]

    def __str__(self):
        s = ''
        for i in self.my_list:
            # for j in i:
            #     if s:
            s += ' '.join(map(str, i))
                # s += str(j)

            s += '\n'
        return s

a = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
# print(ascii(a))
print(a)

# a = [2, 3, 4]
# print(ascii(a))