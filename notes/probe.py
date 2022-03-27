objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
ans = 0
asdd = [objects[0]]
for obj in objects:  # доступная переменная objects
    for i in range(len(asdd)):
        if obj is asdd[i]:
            asdd.insert(i, obj)
        else:
            asdd.append(obj)
    print(asdd)
    asd = list(asdd)
    if asdd:
        ans += 1

print(ans, asdd)

# [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]

# [1, True, 1, 'True', 1, 0, False, 'False']
# for obj in objects:  # доступная переменная objects
#     if obj is next_obj in objects:
#         ans += 1
#     obj_prev = obj
# print(ans)

def c(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    return c(n - 1, k) + c(n - 1, k - 1)

n, k = map(int, input().split())
print(c(n, k))

print(p(*[int(i)for i in input().split()]))

n, k = map(int, input().split())
sz = max(n, k) + 1
c = [[0] * sz for _ in range(sz)]
c[0][0] = 1
for i in range(1, sz):
    for j in range(i + 1):
        c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
print(c[n][k])