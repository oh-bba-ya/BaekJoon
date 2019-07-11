#00시일때 조심하자 만일 else 조건이 없다면 -1이된다.



time = list(map(int,input().split()))
H = time[0]
M = time[1]
if (M <= 44) and (H != 0):
    H -= 1
    M = 60-abs(M-45)
    print(H,M)
elif (M > 44) and (H != 0):
    M -= 45
    print(H,M)
else:
    print(23,M+15)
    
