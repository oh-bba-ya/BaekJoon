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


N = list(map(int,input().split()))
break_even_point = 0
A = N[0]            #고정비용.
B = N[1]            #노트북 생산비용.
C = N[2]            #노트북 판매비용.

# A // (C-B) + 1 = 손익분기점 판매갯수, (C-B)=노트북 판매 이익

if C <= B:                    #노트북 판매가격이 생산비용보다 낮다면 적자가 생기므로 손익분기점이 생길수가 없다.
    break_even_point = -1
else:
    break_even_point = A // (C-B) + 1
print(break_even_point)

#첫번째 도전에는 너무 쓸데없는 식고 변수들을 넣음으로써 실패하였다.
#간단하게 생각해보니 노트북 생산비용 판매비용만 계산해줌으로써 순이익을 찾을 수 있었다.
#노트북 판매순이익을 통해 고정비용을 나눠줌으로써 판매대수를 알 수 있음으로 손익분기점을 찾는게 더 쉬웠다.
