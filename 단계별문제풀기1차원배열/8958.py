count = int(input())
OX = []
for i in range(count):
    OX.append(input())
for i in OX:
    X_sp = i.split('X')
    score = 0
    for j in X_sp:
        size = len(j)
        if size > 0:
            N = (size * (size + 1)) // 2
            score += N
    print(score)
