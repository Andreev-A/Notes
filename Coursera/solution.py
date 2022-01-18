def height(child, tree):
    if child not in tree:
        return 0
    return height(tree[child], tree) + 1


with open('input.txt', 'r', encoding='utf-8') as inf:
    tree, list_all = {}, set()
    n = int(inf.readline())
    for _ in range(n - 1):
        child, parent = inf.readline().split()
        tree.setdefault(child, parent)
        list_all.add(child)
        list_all.add(parent)
[print(name, height(name, tree)) for name in sorted(list_all)]
