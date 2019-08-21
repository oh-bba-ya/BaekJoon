N = int(input())
result = 0
for i in range(1,N+1):        #생성자(M)의 경우 분해합(N)보다 필히 작기에 N의 범위로 충분할것이다.
    N_list = list(map(int,str(i)))        #i를 str화 함으로써 10 -> '1','0' 이런식으로 나뉘어져서 int형으로 들어가게 된다.
    N_sum = i + sum(N_list)                #i = 198일경우 N_sum = 198 + (1+9+8) , 
    if N_sum == N:
        result += i
        break
print(result)
