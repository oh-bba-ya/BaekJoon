while True:            #while은 true일때만 반복
    A , B = map(int,input().split())
    if A == 0 or B ==0:
        break
    print(A + B)
