def fact(num):
    a = 1
    for s in range(1, num + 1):
        a *= s
        yield a
w = 14
for i, el in enumerate(fact(w)):
    print(f'#{i + 1} {el}')