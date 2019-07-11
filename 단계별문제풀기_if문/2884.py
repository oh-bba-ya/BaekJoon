#00시일때 조심하자 만일 else 조건이 없다면 -1이된다.
#또 이런 시간 빼기 에서 45분 이나 어떤 숫자를 뺀다면 60 - 어떤숫자 = x 라 할 때 원래시간에서 +x만큼해주면 되는걸 알았다.



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
    
