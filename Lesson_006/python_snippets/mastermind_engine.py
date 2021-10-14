from random import sample

hidden_number = ''

def number_generator():

    # a = map(str, range(10))
    a = list(map(str, range(10)))
    print(a)
    b = ''.join(sample(a, 4))
    if b[0] == '0':
        b.append(b.pop(0))
    # if b[0] == '0':
    #     b[0], b[1] = b[1], b[0]
    print(int(b))


number_generator()