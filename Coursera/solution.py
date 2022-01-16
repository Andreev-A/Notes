w = open('output.txt ', mode='w', encoding='utf-8')
f = open('input.txt', mode='r', encoding='utf-8')
count, my_input = 0, {}
for line in f:
    my_input[line.strip()] = my_input[line] + 1 if line in my_input else 1
    count += 1
my_out = sorted(my_input.items(), key=lambda x: (-x[1], x[0]))
print(my_out[0][0], file=w)
if my_out[0][1] * 2 <= count:
    print(my_out[1][0], file=w)
w.close()
f.close()
