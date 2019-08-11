N = list(map(int,input().split()))
A = N[0]            #고정비용.
B = N[1]            #노트북 생산비용.
C = N[2]            #노트북 판매비용.
#(C*X)-(A+(B*X)) = P ,P = 순이익.
X = 0        #X=판매갯수.
while True:
    P=(C*X)-(A+(B*X))
    if P > 0:
        break
    X+=1
print(X)

#시간초과로 인해 실패하였다.
