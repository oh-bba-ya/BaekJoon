N = list(map(int,input().split()))
N[0] = A            #고정비용.
N[1] = B            #노트북 생산비용.
N[2] = C            #노트북 판매비용.
#(C*X)-(A+(B*X)) = P ,P = 순이익.
X = 0        #X=판매갯수.
while True:
    P=(C*X)-(A+(B*X))
    if P > 0:
        break
    X+=1
print(X)

#런타임에러가 나왔다.
