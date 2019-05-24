with open('input.txt', 'r', encoding='utf-8') as f:
    first_line = f.readline().split()
    n = int(first_line[0])
    m = int(first_line[1])

    set_ann = set()
    set_borya = set()

    for _ in range(n):
        set_ann.add(int(f.readline()))

    for _ in range(m):
        set_borya.add(int(f.readline()))

    union_set = set_ann | set_borya

    print(len(set_ann & set_borya))

    print(*sorted(set_ann & set_borya))

    print(len(union_set - set_borya))

    print(*sorted(union_set - set_borya))

    print(len(union_set - set_ann))

    print(*sorted(union_set - set_ann))
